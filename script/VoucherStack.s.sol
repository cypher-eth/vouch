// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Script.sol";

contract VoucherStack is Script {
    function getDeployedContract(string memory contractName) internal view returns (address) {
        try vm.envAddress(contractName) {
            return address(vm.envAddress(contractName));
        } catch {
          return address(0);
        }
    }

    function writeContractAddressToFile(
        string memory contractName,
        address contractAddress
    ) internal {
        vm.writeLine(
            string(".env"),
            string(
                abi.encodePacked(
                    contractName,
                    "=",
                    vm.toString(contractAddress)
                )
            )
        );
    }
}
