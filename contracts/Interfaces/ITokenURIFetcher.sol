// SPDX-License-Identifier: GPL-3.0-or-later

pragma solidity ^0.8.16;

interface ITokenURIFetcher {
    function fetchTokenURIData(uint256 id)
        external
        view
        returns (string memory);
}
