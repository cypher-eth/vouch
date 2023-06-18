pragma solidity ^0.8.16;

import "./IMasterContract.sol";

interface IContract is IMasterContract {
    /// @notice Init function that gets called from `BoringFactory.deploy`.
    /// Also kown as the constructor for cloned contracts.

    function initContract( bytes calldata data ) external;

}
