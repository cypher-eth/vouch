pragma solidity 0.8.16;


import "./Tokens/ERC721S.sol";
import "./Descriptors/BolivaresDescriptor.sol";
import "./Utils/BokkyPooBahsDateTimeLibrary.sol";
import "./Utils/Documents.sol";
import "./Vouch.sol";


contract Bolivares is Vouch, Documents, 
    ERC721S("Test Bolivares", "VIBES"), BolivaresDescriptor

 {
    using BokkyPooBahsDateTimeLibrary for uint;
    string public constant VOUCH_NAME = "Zuzalu Bolivares";
    // bytes32 public constant VOUCH_ID = keccak256(abi.encode(VOUCH_NAME));

    string public constant VOUCH_MSG = "I vouch this person had good vibes at Zuzalu";

    uint256 public tokenIds;
    // Vouch public vouch;

    struct VouchData {
        address sender;
        string message;
    } 
    mapping (bytes32  => address) public vouchUser;
    mapping (bytes32 => uint256) public vouchToken;


    mapping (uint256 => bytes32) public tokenInfo;
    mapping (address => string) public userBarcode;
    mapping (address  => uint256) public vouchCount;


    mapping (address  =>  mapping(address  => bool)) public doesVouch;
    mapping (string  => address) public barcodes;
    mapping (string  => VouchData[]) public unvouched;



    // //  ------------------------------------------------------------------------
    // // Register
    // // ------------------------------------------------------------------------

    // TODO: add barcode count? not sure if useful/scaleable

    // User register themselves
    function register (string calldata barcode) external {
        require(barcodes[barcode] == address(0), "Cannot register same bill twice");
        barcodes[barcode] = msg.sender;
        userBarcode[msg.sender] = barcode;
    }

    function unregister (string calldata barcode) external {
        require(barcodes[barcode] == msg.sender);
        // require(userBarcode[msg.sender] == barcode);
        barcodes[barcode] = address(0);
        userBarcode[address(0)] = barcode;
    }

    // if there is an array of unvouched, process the array in chunks
    function processUnvouched(string calldata barcode) external {
        VouchData[] memory vouches = unvouched[barcode];
        require(vouches.length > 0);
        VouchData memory vouchData = unvouched[barcode][vouches.length-1];
        unvouched[barcode].pop();
        _mintVouch(vouchData.sender, barcodes[barcode], vouchData.message);
    }

    function unvouchedCount(string calldata barcode) external view returns (uint) {
        VouchData[] memory vouches = unvouched[barcode];
        return vouches.length;
    }

    // //  ------------------------------------------------------------------------
    // // Vouch
    // // ------------------------------------------------------------------------

    function vouch(string memory barcode, string calldata message) external returns (bool success) {
        address sender = msg.sender;
        address recipient = barcodes[barcode];

        // require(userBarcode[sender] == barcode);
        if (recipient == address(0)) {
            unvouched[barcode].push(VouchData(sender, message));
            return true;
        }
        _mintVouch(sender, recipient, message);

        return true;
    }

    function _mintVouch(address sender, address recipient, string memory message) internal {
        if (!doesVouch[sender][recipient]) {
            doesVouch[sender][recipient] = true;
            vouchCount[recipient]++;
        }

        bytes32 vouchId = generateVouchHash(sender, recipient, message);
        _vouch(recipient, message, sender);

        // Mint onchain vouch, if not exists
        uint256 tokenId = vouchToken[vouchId];
        if (tokenId == 0) {
            // if barcode does not exist, save as unvouched. 
            tokenId = tokenIds++;
            tokenInfo[tokenId] = vouchId;
            _mint(recipient, tokenId);
            vouchToken[vouchId] = tokenId;            
        }
    }

    function verify(string memory barcode) public view returns (uint256)  {
        address user = barcodes[barcode];
    
        // If not registered
        if (user == address(0) ) {
            return 0;
        }
        return vouchCount[user];
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

    /// @notice Return user vouch
    function getVouch(bytes32 _vouchID) public view returns (string memory) {
    }

    function getUserFromVouch(string memory barcode) public view returns (address user) {
        return barcodes[barcode];
    }

    /// @notice Return user vouchIDs
    function getUserVouches(address _user) public view returns (bytes32[] memory) {
    }



}