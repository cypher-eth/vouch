pragma solidity 0.8.17;

import {Test} from "forge-std/Test.sol";
import {console} from "forge-std/console.sol";
import {Bolivares} from "../contracts/Bolivares.sol";

contract BaseTest is Test {
    // CORE Contracts
    Bolivares public bolivares;

    // ACCOUNTS
    address public deployer;

    function setUp() public virtual {
        deployer = address(0x1234);
        vm.label(deployer, "deployer");
        vm.startPrank(deployer);
        vm.deal(deployer, 100 ether);

        bolivares = new Bolivares();
        vm.stopPrank();
    }

}
