pragma solidity 0.8.16;


import "./Tokens/ERC721S.sol";
import "./Descriptors/BolivaresDescriptor.sol";
import "./Utils/BokkyPooBahsDateTimeLibrary.sol";
import "./Utils/Documents.sol";
import "./Vouch.sol";


contract Bolivares is 
    Documents, 
    ERC721S("Test Bolivares", "VIBES"), 
    BolivaresDescriptor
{
    using BokkyPooBahsDateTimeLibrary for uint;
    string public constant VOUCH_NAME = "Zuzalu Bolivares";
    bytes32 public constant VOUCH_ID = keccak256("VOUCH");
    string public constant VOUCH_MSG = "I vouch this person had good vibes at Zuzalu";

    struct VouchInfo {
        address sender;
        uint48 lastUpdateTime;
        uint48 revokedTime;
    }

    /// @notice Mapping from vouchId => vouch info.
    mapping (bytes32 => VouchInfo) public vouchInfo;
    /// @notice Mapping from vouchId => vouch message.
    mapping (bytes32 => string) public vouchMsg;
    /// @notice Mapping from user => user info.
    mapping (address => bytes32[]) public userInfo;

    uint256 public tokenIds;

    /// @notice Mapping from vouch ID => NFT token id.
    mapping (bytes32 => uint256) public vouchToken;
    /// @notice Mapping from NFT token id => vouch ID
    mapping (uint256 => bytes32) public tokenInfo;
    /// @notice Mapping from user address  => barcode
    mapping (address => string) public userBarcode;
    /// @notice Mapping from barcode  => user address
    mapping (string  => address) public barcodes;
    /// @notice How many vouches for an address
    mapping (address  => uint256) public vouchCount;

    struct VouchData {
        address sender;
        string message;
    } 

    mapping (address  =>  mapping(address  => bool)) public doesVouch;
    mapping (string  => VouchData[]) public unvouched;

    // //  ------------------------------------------------------------------------
    // // Register
    // // ------------------------------------------------------------------------

    // TODO: add barcode count? not sure if useful/scaleable
    /**
     * @notice Registers a user by barcode
     * @param barcode user's unique barcode to register
     */
    function register(string calldata barcode) external {
        require(barcodes[barcode] == address(0), "Cannot register same bill twice");
        barcodes[barcode] = msg.sender;
        userBarcode[msg.sender] = barcode;
    }

    /**
     * @notice Unregister user
     * @param barcode user's barcode
     */
    function unregister(string calldata barcode) external {
        require(barcodes[barcode] == msg.sender);
        // require(userBarcode[msg.sender] == barcode);
        barcodes[barcode] = address(0);
        userBarcode[address(0)] = barcode;
    }

    // if there is an array of unvouched, process the array in chunks
    /**
     * @notice Processes the unvouched entry for a given barcode
     * @param barcode user's barcode
     */
    function processUnvouched(string calldata barcode) external {
        VouchData[] memory vouches = unvouched[barcode];
        require(vouches.length > 0);
        VouchData memory vouchData = vouches[vouches.length-1];
        unvouched[barcode].pop();
        _mintVouch(vouchData.sender, barcodes[barcode], vouchData.message);
    }

    /**
     * @param barcode user's barcode
     * @return number of unvouched vounches for the given barcode
     */
    function unvouchedCount(string calldata barcode) external view returns (uint) {
        VouchData[] memory vouches = unvouched[barcode];
        return vouches.length;
    }

    // //  ------------------------------------------------------------------------
    // // Vouch
    // // ------------------------------------------------------------------------

    /**
     * @notice Vouches for the user associated with a barcode
     * @param barcode barcode of the user for whom to vouch
     * @param message message to associate with the vouch
     * @return true if success
     */    
    function vouch(string memory barcode, string calldata message) external returns (bool success) {
        address sender = msg.sender;
        address recipient = barcodes[barcode];

        require(sender != recipient, "Vouch for yourself is not allowed");

        // require(userBarcode[sender] == barcode);
        if (recipient == address(0)) {
            unvouched[barcode].push(VouchData(sender, message));
            return true;
        }
        _mintVouch(sender, recipient, message);

        return true;
    }

    function verify(string memory barcode) public view returns (uint256)  {
        address user = barcodes[barcode];
        // If not registered
        if (user == address(0) ) {
            return 0;
        }
        return vouchCount[user];
    }


    /**
     * @notice Creates a new vouch for a recipient
     * @param recipient address of the user for whom to vouch
     * @param message message of the vouch
     * @param sender address of the voucher
     */    
    function _vouch(address recipient, string memory message, address sender) internal {
        bytes32 hashed = generateVouchHash(sender,recipient,message);

        // Update vouch
        _updateVouch(hashed, sender); 
        vouchMsg[hashed] = message;
    }

    /**
     * @dev Internal function to update an existing vouch or create a new one
     * @param vouchId ID of the vouch
     * @param sender address of the voucher
     */    
    function _updateVouch(bytes32 vouchId, address sender) private {
        if ( vouchInfo[vouchId].lastUpdateTime == 0 ) { 
            userInfo[sender].push(vouchId);
        }
        vouchInfo[vouchId] = VouchInfo(sender, uint48(block.timestamp), 0);
    }


    /**
     * @dev Internal function to to mint a new vouch
     * @param sender address of the sender creating the vouch
     * @param recipient voucher recipient address
     * @param vouchId ID of the vouch
     * @param message message of the vouch.
     */
    function _mintVouch(address sender, address recipient, string memory message) internal {
        if (!doesVouch[sender][recipient]) {
            doesVouch[sender][recipient] = true;
            vouchCount[recipient]++;
        }

        bytes32 vouchId = generateVouchHash(sender, recipient, message);
        _vouch(recipient, message, sender, vouchId);

        // Mint onchain vouch, if not exists
        uint256 tokenId = vouchToken[vouchId];
        if (tokenId == 0) {
            tokenId = tokenIds++;
            tokenInfo[tokenId] = vouchId;
            _mint(recipient, tokenId);
            vouchToken[vouchId] = tokenId;            
        }
    }

    // ------------------------------------------------------------------------
    // Revoke
    // ------------------------------------------------------------------------

    /**
     * @notice Revokes a voucher by vouchId
     * @param vouchId ID of the vouch
     */
    function revoke(bytes32 vouchId) external returns (bool success) {
        return _revoke(vouchId, msg.sender );
    }

    /**
     * @notice Revokes a voucher by vouchId
     * @param vouchId ID of the vouch
     */
    function _revoke( bytes32 vouchId, address sender) private returns (bool success) {
        require(vouchInfo[vouchId].sender == sender, "Sender did not vouch");
        vouchInfo[vouchId].revokedTime = uint48(block.timestamp);
        return true;
    }


    // ------------------------------------------------------------------------
    // NFT Descriptors
    // ------------------------------------------------------------------------

    function tokenURI(uint256 id) public view override returns (string memory) {
        return dataURI(id, lastUpdated(tokenInfo[id]) ,vouchSender(tokenInfo[id]), ownerOf(id), VOUCH_MSG, userBarcode[ownerOf(id)]);
    }

    // ------------------------------------------------------------------------
    // Documents
    // ------------------------------------------------------------------------

    function setDocument(string calldata _name, string calldata _data) external {
        _setDocument( _name, _data);
    }

    function setDocuments(string[] calldata _name, string[] calldata _data) external {
        uint256 numDocs = _name.length;
        for (uint256 i = 0; i < numDocs; i++) {
            _setDocument( _name[i], _data[i]);
        }
    }

    function removeDocument(string calldata _name) external {
        _removeDocument(_name);
    }

    // ------------------------------------------------------------------------
    // Getters
    // ------------------------------------------------------------------------

    function verifyVouchSig(bytes32 hash, bytes calldata sig) public pure returns (bool success) {
        if ( address(0) == ecrecoverFromSig(hash, sig)) return false;
        return true;
    }

    function revoked(bytes32 vouchId) public view returns (uint256) {
        return uint256(vouchInfo[vouchId].revokedTime);
    }

    function lastUpdated(bytes32 vouchId) public view returns (uint256) {
        return uint256(vouchInfo[vouchId].lastUpdateTime);
    }

    function vouchSender(bytes32 vouchId) public view returns (address) {
        return vouchInfo[vouchId].sender;
    }


    /// @notice Return user vouch
    function getVouch(bytes32 _vouchID) public view returns (string memory) {
    }

    function getUserFromVouch(string memory barcode) public view returns (address user) {
        return barcodes[barcode];
    }

    /// @notice Return user vouchIDs
    function getUserVouches(address _user) public view returns (bytes32[] memory) {
    }



    // ------------------------------------------------------------------------
    // ECDSA Signatures
    // ------------------------------------------------------------------------

    // ------------------------------------------------------------------------
    // ecrecover from a signature rather than the signature in parts [v, r, s]
    // The signature format is a compact form {bytes32 r}{bytes32 s}{uint8 v}.
    // Compact means, uint8 is not padded to 32 bytes.
    //
    // An invalid signature results in the address(0) being returned, make
    // sure that the returned result is checked to be non-zero for validity
    //
    // Parts from https://gist.github.com/axic/5b33912c6f61ae6fd96d6c4a47afde6d
    // ------------------------------------------------------------------------

    function ecrecoverFromSig(bytes32 hash, bytes memory sig) public pure returns (address recoveredAddress) {
        if (sig.length == 65) {
            bytes32 r;
            bytes32 s;
            uint8 v;
            // ecrecover takes the signature parameters, and the only way to get them
            // currently is to use assembly.
            /// @solidity memory-safe-assembly
            assembly {
                r := mload(add(sig, 0x20))
                s := mload(add(sig, 0x40))
                v := byte(0, mload(add(sig, 0x60)))
            }
            return tryRecover(hash, v, r, s);
        } else {
            return address(0);
        }
    }


    /**
     * @dev Overload of {ECDSA-tryRecover} that receives the `v`,
     * `r` and `s` signature fields separately.
     *
     * _Available since v4.3._
     */
    function tryRecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s) internal pure returns (address) {
        // EIP-2 still allows signature malleability for ecrecover(). Remove this possibility and make the signature
        // unique. Appendix F in the Ethereum Yellow paper (https://ethereum.github.io/yellowpaper/paper.pdf), defines
        // the valid range for s in (301): 0 < s < secp256k1n ÷ 2 + 1, and for v in (302): v ∈ {27, 28}. Most
        // signatures from current libraries generate a unique signature with an s-value in the lower half order.
        //
        // If your library generates malleable signatures, such as s-values in the upper range, calculate a new s-value
        // with 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 - s1 and flip v from 27 to 28 or
        // vice versa. If your library also generates signatures with 0/1 for v instead 27/28, add 27 to v to accept
        // these malleable signatures as well.
        if (uint256(s) > 0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF5D576E7357A4501DDFE92F46681B20A0) {
            return address(0);
        }

        // If the signature is valid (and not malleable), return the signer address
        address signer = ecrecover(hash, v, r, s);
        if (signer == address(0)) {
            return address(0);
        }

        return signer;
    }



}