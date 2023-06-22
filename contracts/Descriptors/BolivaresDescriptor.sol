
/// @title A library used to construct ERC721 token URIs and SVG images
/// @dev From the Nouns NFT descriptor

pragma solidity 0.8.16;

import "./NFTDescriptor.sol";
import "../Utils/BokkyPooBahsDateTimeLibrary.sol";

abstract contract BolivaresDescriptor is NFTDescriptor {

    using BokkyPooBahsDateTimeLibrary for uint;
    uint8 private constant _ADDRESS_LENGTH = 20;
    bytes16 private constant _SYMBOLS = "0123456789abcdef";

    // ------------------------------------------------------------------------
    // NFT Descriptors
    // ------------------------------------------------------------------------

    /**
     * @notice Given a token ID and seed, construct a base64 encoded data URI for an NFT.
     */
    function dataURI(uint256 tokenId, uint256 _lastUpdate, address _sender, address _recipient, string memory _msg, string memory _barcode) public view returns (string memory) {
        string memory name = string(abi.encodePacked('Vouch #', toString(tokenId)));

        string memory image = string(abi.encodePacked('data:image/svg+xml;base64,', Base64.encode(bytes(_vouchImage(tokenId, _lastUpdate,_sender,_recipient, _msg, _barcode )))));
        string memory description = string(abi.encodePacked('This NFT represents a signed message from a sender to this address. This NFT cannot be transfered.'));
        string memory attributes = generateAttributesList(tokenId, _msg);

        return genericDataURI(name, description, image, attributes);
    }

    /**
     * @notice Given a token ID, construct a base64 encoded SVG.
     */
    function _vouchImage(uint _tokenId, uint256 _lastUpdate, address _sender, address _recipient, string memory _msg, string memory _barcode) internal view returns (string memory output) {
        output = '<svg xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMin meet" viewBox="0 0 350 350"><style>.base { fill: #ffeeff; font-family: serif; font-size: 15px; }</style><rect width="100%" height="100%" fill="#19473f" /><text x="240" y="40" class="base">';
        output = string(abi.encodePacked(output, timestampToString(_lastUpdate), '</text><text x="20" y="80" class="base">'));
        output = string(abi.encodePacked(output, _msg, '</text><text x="20" y="265" class="base">from: </text><text x="20" y="290" class="base">'));
        output = string(abi.encodePacked(output, _barcode, '</text><text x="240" y="320" class="base">vouch # ' ,toString(_tokenId) , '</text></svg>'));
    }

    /**
     * @notice NFT Atrributes based on Token ID
     */
    function generateAttributesList(uint256 tokenId, string memory vouch) public view returns (string memory) {
        return string(
            abi.encodePacked(
                '{"trait_type":"Vouch","value":"', vouch,'"},',
                '{"trait_type":"Vouch ID","value":', toString(tokenId),'}'
            )
        );
    }


    /**
     * @notice Given a name, description, and seed, construct a base64 encoded data URI.
     */
    function genericDataURI(
        string memory _name,
        string memory _description,
        string memory _image,
        string memory _attributes
    ) public view returns (string memory) {
        TokenURIParams memory params = TokenURIParams({
            name: _name,
            description: _description,
            image: _image,
            attributes: _attributes
        });
        return constructTokenURI(params);
    }

    function timestampToDate(uint timestamp) public pure returns (uint year, uint month, uint day) {
        (year, month, day) = BokkyPooBahsDateTimeLibrary.timestampToDate(timestamp);
    }

    function timestampToString(uint timestamp) public pure returns (string memory) {
        (uint year, uint month, uint day) = BokkyPooBahsDateTimeLibrary.timestampToDate(timestamp);
        return string(abi.encodePacked(dayOfMonthString(day), ' ', monthStringShort(month), ' ', toString(year)));
    }

    function monthStringShort (uint month) public pure returns (string memory) {
        if (month == 1) return "Jan";
        if (month == 2) return "Feb";
        if (month == 3) return "Mar";
        if (month == 4) return "Apr";
        if (month == 5) return "May";
        if (month == 6) return "Jun";
        if (month == 7) return "Jul";
        if (month == 8) return "Aug";
        if (month == 9) return "Sep";
        if (month == 10) return "Oct";
        if (month == 11) return "Nov";
        if (month == 12) return "Dec";
        return "";
    }

    function dayOfMonthString (uint dayOfMonth) public pure returns (string memory) {
        if (dayOfMonth == 1) return "1st";
        if (dayOfMonth == 2) return "2nd";
        if (dayOfMonth == 3) return "3rd";
        if (dayOfMonth == 21) return "21st";
        if (dayOfMonth == 22) return "22nd";
        if (dayOfMonth == 23) return "23rd";
        if (dayOfMonth == 31) return "31st";
        if (dayOfMonth < 31 && dayOfMonth > 0 ) {
            return string(abi.encodePacked(toString(dayOfMonth), 'th'));
        }
    }

    function toString(uint256 value) internal pure returns (string memory) {
        // Inspired by OraclizeAPI's implementation - MIT licence
        // https://github.com/oraclize/ethereum-api/blob/b42146b063c7d6ee1358846c198246239e9360e8/oraclizeAPI_0.4.25.sol

        if (value == 0) {
            return "0";
        }
        uint256 temp = value;
        uint256 digits;
        while (temp != 0) {
            digits++;
            temp /= 10;
        }
        bytes memory buffer = new bytes(digits);
        while (value != 0) {
            digits -= 1;
            buffer[digits] = bytes1(uint8(48 + uint256(value % 10)));
            value /= 10;
        }
        return string(buffer);
    }

    /**
     * @dev Converts a `uint256` to its ASCII `string` hexadecimal representation with fixed length.
     */
    function toHexString(uint256 value, uint256 length) internal pure returns (string memory) {
        bytes memory buffer = new bytes(2 * length + 2);
        buffer[0] = "0";
        buffer[1] = "x";
        for (uint256 i = 2 * length + 1; i > 1; --i) {
            buffer[i] = _SYMBOLS[value & 0xf];
            value >>= 4;
        }
        require(value == 0, "Strings: hex length insufficient");
        return string(buffer);
    }

    /**
     * @dev Converts an `address` with fixed length of 20 bytes to its not checksummed ASCII `string` hexadecimal representation.
     */
    function toHexString(address addr) internal pure returns (string memory) {
        return toHexString(uint256(uint160(addr)), _ADDRESS_LENGTH);
    }


}