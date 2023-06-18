pragma solidity 0.8.17;

import {Test} from "forge-std/Test.sol";
import {console} from "forge-std/console.sol";

import {BaseTest} from "./BaseTest.t.sol";
import {StringUtils} from "./utils/StringUtils.sol";

contract BolivaresTest is BaseTest {
    using StringUtils for string;

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
        bolivares.register(barcode);
        assert(bolivares.getUserFromVouch(barcode) == user1);
        assert(barcode.equal(bolivares.userBarcode(user1)));

        vm.expectRevert("Cannot register same bill twice");
        bolivares.register(barcode);
        vm.stopPrank();
    }

    function testRegisterFuzz(string memory barcode) public {
        vm.startPrank(user1);
        bolivares.register(barcode);
        assert(bolivares.getUserFromVouch(barcode) == user1);
        assert(barcode.equal(bolivares.userBarcode(user1)));

        vm.expectRevert("Cannot register same bill twice");
        bolivares.register(barcode);
        vm.stopPrank();
    }

}
