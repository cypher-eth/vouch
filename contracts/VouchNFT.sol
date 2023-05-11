pragma solidity 0.8.16;


import "./Tokens/ERC721S.sol";
import "./Descriptors/VouchDescriptor.sol";
import "./Utils/BokkyPooBahsDateTimeLibrary.sol";

interface Vouch {
    function generateVouchHash(address recipient, string memory message) external view returns (bytes32 hash);
    function vouchFromSig (address recipient, string calldata message, bytes calldata sig) external returns (bool success);
    function lastUpdated(bytes32 vouchId) external view returns (uint256);
    function vouchSender(bytes32 vouchId) external view returns (address);
    function vouchMsg(bytes32 vouchId) external view returns (string calldata);
    function userInfo(address user) external view returns (bytes32[] calldata);
    function doesVouch(address _sender, address recipient) external view returns (bool);
}


contract VouchNFT is 
    ERC721S("Vouch NFT", "VOUCH"), VouchDescriptor

 {
    using BokkyPooBahsDateTimeLibrary for uint;
    bytes32 public constant VOUCH_ID = keccak256("VOUCH");
    uint256 public tokenIds;
    Vouch public vouch;

    mapping (uint256 => bytes32) public tokenInfo;
    mapping (bytes32 => uint256) public vouchToken;

    constructor(address _vouch) {
        vouch = Vouch(_vouch);
    }



    // //  ------------------------------------------------------------------------
    // // Vouching
    // // ------------------------------------------------------------------------

    function mintVouchFromSig (address recipient, string calldata message, bytes calldata sig) external returns (bool success) {      

        bytes32 vouchId = vouch.generateVouchHash(recipient, message);
        uint tokenId = vouchToken[vouchId];

        // Mint onchain vouch, if not exists
        if (tokenId == 0) {
            tokenId = tokenIds++;
            tokenInfo[tokenId] = vouchId;
            _mint(recipient, tokenId);
            vouchToken[vouchId] = tokenId;
        }

        return vouch.vouchFromSig(recipient, message, sig);
    }

    function mintVouch(address recipient, bytes32 vouchId) external returns (bool success) {
        // require(); 
        uint256 tokenId = vouchToken[vouchId];
        // Mint onchain vouch, if not exists
        if (tokenId == 0) {
            tokenId = tokenIds++;
            tokenInfo[tokenId] = vouchId;
            _mint(recipient, tokenId);
            vouchToken[vouchId] = tokenId;
        }
        return true;
    }


    // ------------------------------------------------------------------------
    // NFT Descriptors
    // ------------------------------------------------------------------------

    function tokenURI(uint256 id) public view override returns (string memory) {
        return dataURI(id, vouch.lastUpdated(tokenInfo[id]) ,vouch.vouchSender(tokenInfo[id]), vouch.vouchMsg(tokenInfo[id]));
    }

    // ------------------------------------------------------------------------
    // Getters
    // ------------------------------------------------------------------------

    /// @notice Return user vouches
    function getOwnerVouches(address _owner) public view returns (bytes32[] memory) {
        return vouch.userInfo(_owner);
    }

    /// @notice Returns true if sender has vouched for recipient
    function doesVouch(address sender, address recipient) public view returns (bool) {
        return vouch.doesVouch(sender,recipient);

    }


}