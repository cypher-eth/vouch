pragma solidity 0.8.16;


import "./Tokens/ERC721S.sol";
import "./Descriptors/BolivaresDescriptor.sol";
import "./Utils/BokkyPooBahsDateTimeLibrary.sol";
import "./Utils/BokkyPooBahsDateTimeLibrary.sol";
import "./Vouch.sol";


contract Bolivares is Vouch, 
    ERC721S("Test Bolivares", "VIBES"), BolivaresDescriptor

 {
    using BokkyPooBahsDateTimeLibrary for uint;
    string public constant VOUCH_NAME = "Zuzalu Bolivares";
    // bytes32 public constant VOUCH_ID = keccak256(abi.encode(VOUCH_NAME));

    string public constant REGISTER_MSG = "I vouch that this person recieved a Bolivares in Zuzalu";
    string public constant VOUCH_MSG = "I vouch this person had good vibes at Zuzalu";

    uint256 public tokenIds;
    // Vouch public vouch;

    mapping (bytes32  => address) public userCommit;
    mapping (bytes32 => uint256) public vouchToken;

    mapping (uint256 => bytes32) public tokenInfo;
    mapping (address => uint256) public userInvites;
    mapping (address => string) public userBarcode;
    mapping (address  => uint256) public vouchCount;
    mapping (address  =>  mapping (address  => bool)) public doesVouch;
    mapping (string  => bool) public barcodes;



    // //  ------------------------------------------------------------------------
    // // Register
    // // ------------------------------------------------------------------------


    // function register () external {
    //     vouch.vouch(msg.sender, REGISTER_VOUCH);
    // }

    // function commit (address user, string memory barcode) external {
    //     // only bouncer
    //     // Adds person to the allowlist
    //     commit = keccak256(abi.encode(address(this), VOUCH_ID, barcode));
    //     userCommit[commit] = user;
    // }

    // User register another user
    function register (address user, string memory barcode) external {
        barcodes[barcode] = true;
        userBarcode[user] = barcode;
        // vouch.vouch(user, REGISTER_MSG);
        bytes32 commit = keccak256(abi.encode(address(this), VOUCH_ID, barcode));
        userCommit[commit] = user;
    }

    // Bouncer confirm
    function confirm (address user, string memory barcode, uint256 invites) external {
        // only bouncer
        require(keccak256(abi.encode(barcode)) == keccak256(abi.encode(userBarcode[user])));
        // Adds person to the allowlist
        bytes32 commit = keccak256(abi.encode(address(this), VOUCH_ID, barcode));
        userInvites[user] = invites;

    }

    // //  ------------------------------------------------------------------------
    // // Vouch
    // // ------------------------------------------------------------------------


    function vouch(address recipient) external {
        // Verify only vouch counted once
        require(!doesVouch[msg.sender][recipient]);
        doesVouch[msg.sender][recipient] = true;

        // mint vouch to recipirent
        bytes32 vouchId = generateVouchHash(msg.sender, recipient, VOUCH_MSG);
        // bytes32 vouchId = keccak256(abi.encode(recipient, msg.sender));
  
        _vouch(recipient, VOUCH_MSG, msg.sender);

        uint256 tokenId = vouchToken[vouchId];
        // Mint onchain vouch, if not exists
        if (tokenId == 0) {
            tokenId = tokenIds++;
            tokenInfo[tokenId] = vouchId;
            _mint(recipient, tokenId);
            vouchToken[vouchId] = tokenId;
        }

        // increment vouch count
        vouchCount[recipient]++;

    }

    function verify(string memory barcode) public view returns (uint256)  {
        bytes32 commit = keccak256(abi.encode(address(this), VOUCH_ID, barcode));
        address user = getUserFromCommit(commit);
    
        // If not registered
        if (user == address(0) ) {
            return 0;
        }
        return vouchCount[user];
    }


    function getUserFromCommit(bytes32 commit) public view returns (address user) {
        return userCommit[commit];
    }

    // ------------------------------------------------------------------------
    // NFT Descriptors
    // ------------------------------------------------------------------------

    // function tokenURI(uint256 id) public view override returns (string memory) {
    //     return dataURI(id, lastUpdated(tokenInfo[id]) ,vouchSender(tokenInfo[id]), vouchMsg(tokenInfo[id]));
    // }

    function tokenURI(uint256 id) public view override returns (string memory) {
        return dataURI(id, lastUpdated(tokenInfo[id]) ,vouchSender(tokenInfo[id]), ownerOf(id), VOUCH_MSG, userBarcode[ownerOf(id)]);
    }


    // //  ------------------------------------------------------------------------
    // // Minting
    // // ------------------------------------------------------------------------

    // function mintVouchFromSig (address recipient, string calldata message, bytes calldata sig) external returns (bool success) {      

    //     bytes32 vouchId = vouch.generateVouchHash(recipient, message);
    //     uint tokenId = vouchToken[vouchId];

    //     // Mint onchain vouch, if not exists
    //     if (tokenId == 0) {
    //         tokenId = tokenIds++;
    //         tokenInfo[tokenId] = vouchId;
    //         _mint(recipient, tokenId);
    //         vouchToken[vouchId] = tokenId;
    //     }

    //     return vouch.vouchFromSig(recipient, message, sig);
    // }

    // function mintVouch(address recipient, bytes32 vouchId) external returns (bool success) {
    //     // require(); 
    //     uint256 tokenId = vouchToken[vouchId];
    //     // Mint onchain vouch, if not exists
    //     if (tokenId == 0) {
    //         tokenId = tokenIds++;
    //         tokenInfo[tokenId] = vouchId;
    //         _mint(recipient, tokenId);
    //         vouchToken[vouchId] = tokenId;
    //     }
    //     return true;
    // }



    // ------------------------------------------------------------------------
    // Getters
    // ------------------------------------------------------------------------

    // /// @notice Return user vouches
    // function getOwnerVouches(address _owner) public view returns (bytes32[] memory) {
    //     return vouch.userInfo(_owner);
    // }

    // /// @notice Returns true if sender has vouched for recipient
    // function doesVouch(address sender, address recipient) public view returns (bool) {
    //     return vouch.doesVouch(sender,recipient);

    // }


}