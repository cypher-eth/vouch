// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "./VoucherStack.s.sol";
import {Bolivares} from "../contracts/Bolivares.sol";

contract VoucherScript is VoucherStack {
    Bolivares bolivares;

    function run() public {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");
        vm.startBroadcast(deployerPrivateKey);

        if (address(bolivares) == address(0)) {
            address bolivaresAddress = getDeployedContract("BOLIVARES");

            if(bolivaresAddress == address(0)) {
                bolivares = new Bolivares();
                writeContractAddressToFile("BOLIVARES", address(bolivares));
            } else {
                bolivares = Bolivares(bolivaresAddress);
            }
        }
    }
}
