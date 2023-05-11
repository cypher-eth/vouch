pragma solidity 0.8.16;

import "./Utils/BokkyPooBahsDateTimeLibrary.sol";

contract Vouch {
    using BokkyPooBahsDateTimeLibrary for uint;
    bytes32 public constant VOUCH_ID = keccak256("VOUCH");

    struct VouchInfo {
        address sender;
        uint48 lastUpdateTime;
        uint48 revokedTime;
    }

    /// @notice Mapping from vouchId => vouch info.
    mapping (bytes32 => VouchInfo) public vouchInfo;
    mapping (bytes32 => string) public vouchMsg;

    /// @notice Mapping from user => user info.
    mapping (address => bytes32[]) public userInfo;

    /// @dev reentrancy guard
    uint8 internal constant _not_entered = 1;
    uint8 internal constant _entered = 2;
    uint8 internal _entered_state;

    modifier nonreentrant() {
        require(_entered_state == _not_entered);
        _entered_state = _entered;
        _;
        _entered_state = _not_entered;
    }


    // ------------------------------------------------------------------------
    // Vouching
    // ------------------------------------------------------------------------

    // function vouch(address recipient, string calldata message) external returns (bool success) {
    //     return _vouch(recipient,message, msg.sender );
    // }

    /// @notice Generates hash 
    function generateVouchHash(address sender, address recipient, string memory message) public view returns (bytes32 hash) {
        hash = keccak256(abi.encode(address(this), VOUCH_ID, sender, recipient, message));
    }

    // function vouchFromSig (address recipient, string calldata message, bytes calldata sig) external nonreentrant returns (bool success) {
    //     bytes32 hashed = generateVouchHash(recipient,message);
    //     address sender = ecrecoverFromSig(hashed, sig);
    //     require(address(0) != sender, "Invalid vouch signature");
    //     return _vouch(recipient,message, sender);
    // }

    function vouchOffchain(bytes32 vouchId) external nonreentrant returns (bool success) {
        return _updateVouch(vouchId, msg.sender);
    }

    function vouchOffchainFromSig(bytes32 vouchId, bytes calldata sig) external nonreentrant returns (bool success) {
        address sender = ecrecoverFromSig(vouchId, sig);
        require(address(0) != sender, "Invalid vouch signature");
        return _updateVouch(vouchId, sender);
    }

    function _vouch(address recipient, string memory message, address sender) internal returns (bool success) {
        bytes32 hashed = generateVouchHash(sender,recipient,message);

        // Update vouch
        _updateVouch(hashed, sender); 
        vouchMsg[hashed] = message;

        return true;
    }

    function _updateVouch(bytes32 vouchId, address sender) private returns (bool success) {
        if ( vouchInfo[vouchId].lastUpdateTime == 0 ) { 
            userInfo[sender].push(vouchId);
        }
        vouchInfo[vouchId] = VouchInfo(sender, uint48(block.timestamp), 0);
        return true;
    }


    // ------------------------------------------------------------------------
    // Revoke
    // ------------------------------------------------------------------------

    function revoke( bytes32 vouchId) external returns (bool success) {
        return _revoke(vouchId, msg.sender );
    }

    function _revoke( bytes32 vouchId, address sender) private returns (bool success) {
        require(vouchInfo[vouchId].sender == sender, "Sender did not vouch");
        vouchInfo[vouchId].revokedTime = uint48(block.timestamp);
        return true;
    }

    // ------------------------------------------------------------------------
    // Getters
    // ------------------------------------------------------------------------
    // /// @notice Returns true if sender has vouched for recipient
    // function doesVouch(address _sender, address recipient) public view returns (bool) {
    //     uint256 count = userInfo[recipient].length;
    //     bytes32[] memory vouches = userInfo[recipient];
    //     for(uint i = 0; i < count; ) {
    //         if (vouchInfo[vouches[i]].sender == _sender) {
    //             return true;
    //         }
    //         unchecked {
    //             ++i;
    //         }
    //     }
    //     return false;
    // }

    // function verifyVouch(address recipient, string calldata message, bytes calldata sig) public view returns (bool success) {
    //     verifyVouchSig(generateVouchHash(recipient,message),sig);
    // }

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