pragma solidity 0.8.17;

import {Test} from "forge-std/Test.sol";
import {console} from "forge-std/console.sol";

import {BaseTest} from "./BaseTest.sol";

contract BolivaresTest is BaseTest {
    // ACCOUNTS
    address public user1;
    address public user2;
    address public user3;

    function setUp() public virtual override {
        super.setUp();
        user1 = vm.addr(1);
        user2 = vm.addr(2);
        user3 = vm.addr(3);
    }

    function testRegister() public {
        vm.startPrank(user1);
        string memory barcode = "12345";
        bolivares.register(user1, barcode);
        assert(bolivares.getUserFromVouch(barcode) == account.address);
        assert(bolivares.userBarcode(user1.address) == barcode);

        vm.expectRevert("Cannot register same bill twice");
        bolivares.register(user1, barcode);
        vm.stopPrank();
    }

}
