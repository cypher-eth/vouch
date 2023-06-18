
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from woke.development.core import Contract, Library, Address, Account, Chain, RequestType
from woke.development.primitive_types import *
from woke.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.contracts.Descriptors.VouchDescriptor import VouchDescriptor
from pytypes.contracts.Tokens.ERC721S import ERC721S



class Vouch(Contract):
    """
    [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#8)
    """
    _abi = {b'(\xdag\n': {'inputs': [{'internalType': 'address', 'name': '_sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}], 'name': 'doesVouch', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc4\xce\xeb\xb2': {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'string', 'name': 'message', 'type': 'string'}], 'name': 'generateVouchHash', 'outputs': [{'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\x06\x0e\xb2\xf5': {'inputs': [{'internalType': 'bytes32', 'name': 'vouchId', 'type': 'bytes32'}], 'name': 'lastUpdated', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x19Y\xa0\x02': {'inputs': [{'internalType': 'address', 'name': 'user', 'type': 'address'}], 'name': 'userInfo', 'outputs': [{'internalType': 'bytes32[]', 'name': '', 'type': 'bytes32[]'}], 'stateMutability': 'view', 'type': 'function'}, b'4\x06\x1cp': {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'string', 'name': 'message', 'type': 'string'}, {'internalType': 'bytes', 'name': 'sig', 'type': 'bytes'}], 'name': 'vouchFromSig', 'outputs': [{'internalType': 'bool', 'name': 'success', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'1\xe1\xf5\xf7': {'inputs': [{'internalType': 'bytes32', 'name': 'vouchId', 'type': 'bytes32'}], 'name': 'vouchMsg', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf6\xbb\x93\xec': {'inputs': [{'internalType': 'bytes32', 'name': 'vouchId', 'type': 'bytes32'}], 'name': 'vouchSender', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Vouch:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Vouch]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, Vouch, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[Vouch]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @overload
    def generateVouchHash(self, recipient: Union[Account, Address], message: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#9)

        Args:
            recipient: address
            message: string
        Returns:
            bytes32
        """
        ...

    @overload
    def generateVouchHash(self, recipient: Union[Account, Address], message: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#9)

        Args:
            recipient: address
            message: string
        Returns:
            bytes32
        """
        ...

    @overload
    def generateVouchHash(self, recipient: Union[Account, Address], message: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#9)

        Args:
            recipient: address
            message: string
        Returns:
            bytes32
        """
        ...

    @overload
    def generateVouchHash(self, recipient: Union[Account, Address], message: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#9)

        Args:
            recipient: address
            message: string
        Returns:
            bytes32
        """
        ...

    def generateVouchHash(self, recipient: Union[Account, Address], message: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#9)

        Args:
            recipient: address
            message: string
        Returns:
            bytes32
        """
        return self._execute(self.chain, request_type, "c4ceebb2", [recipient, message], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def vouchFromSig(self, recipient: Union[Account, Address], message: str, sig: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#10)

        Args:
            recipient: address
            message: string
            sig: bytes
        Returns:
            bool
        """
        ...

    @overload
    def vouchFromSig(self, recipient: Union[Account, Address], message: str, sig: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#10)

        Args:
            recipient: address
            message: string
            sig: bytes
        Returns:
            bool
        """
        ...

    @overload
    def vouchFromSig(self, recipient: Union[Account, Address], message: str, sig: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#10)

        Args:
            recipient: address
            message: string
            sig: bytes
        Returns:
            bool
        """
        ...

    @overload
    def vouchFromSig(self, recipient: Union[Account, Address], message: str, sig: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#10)

        Args:
            recipient: address
            message: string
            sig: bytes
        Returns:
            bool
        """
        ...

    def vouchFromSig(self, recipient: Union[Account, Address], message: str, sig: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#10)

        Args:
            recipient: address
            message: string
            sig: bytes
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "34061c70", [recipient, message, sig], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def lastUpdated(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#11)

        Args:
            vouchId: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def lastUpdated(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#11)

        Args:
            vouchId: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def lastUpdated(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#11)

        Args:
            vouchId: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def lastUpdated(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#11)

        Args:
            vouchId: bytes32
        Returns:
            uint256
        """
        ...

    def lastUpdated(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#11)

        Args:
            vouchId: bytes32
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "060eb2f5", [vouchId], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def vouchSender(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#12)

        Args:
            vouchId: bytes32
        Returns:
            address
        """
        ...

    @overload
    def vouchSender(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#12)

        Args:
            vouchId: bytes32
        Returns:
            address
        """
        ...

    @overload
    def vouchSender(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#12)

        Args:
            vouchId: bytes32
        Returns:
            address
        """
        ...

    @overload
    def vouchSender(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#12)

        Args:
            vouchId: bytes32
        Returns:
            address
        """
        ...

    def vouchSender(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#12)

        Args:
            vouchId: bytes32
        Returns:
            address
        """
        return self._execute(self.chain, request_type, "f6bb93ec", [vouchId], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def vouchMsg(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#13)

        Args:
            vouchId: bytes32
        Returns:
            string
        """
        ...

    @overload
    def vouchMsg(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#13)

        Args:
            vouchId: bytes32
        Returns:
            string
        """
        ...

    @overload
    def vouchMsg(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#13)

        Args:
            vouchId: bytes32
        Returns:
            string
        """
        ...

    @overload
    def vouchMsg(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#13)

        Args:
            vouchId: bytes32
        Returns:
            string
        """
        ...

    def vouchMsg(self, vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#13)

        Args:
            vouchId: bytes32
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "31e1f5f7", [vouchId], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def userInfo(self, user: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[bytes32]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#14)

        Args:
            user: address
        Returns:
            bytes32[]
        """
        ...

    @overload
    def userInfo(self, user: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#14)

        Args:
            user: address
        Returns:
            bytes32[]
        """
        ...

    @overload
    def userInfo(self, user: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#14)

        Args:
            user: address
        Returns:
            bytes32[]
        """
        ...

    @overload
    def userInfo(self, user: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[bytes32]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#14)

        Args:
            user: address
        Returns:
            bytes32[]
        """
        ...

    def userInfo(self, user: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[bytes32], TransactionAbc[List[bytes32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#14)

        Args:
            user: address
        Returns:
            bytes32[]
        """
        return self._execute(self.chain, request_type, "1959a002", [user], True if request_type == "tx" else False, List[bytes32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def doesVouch(self, _sender: Union[Account, Address], recipient: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#15)

        Args:
            _sender: address
            recipient: address
        Returns:
            bool
        """
        ...

    @overload
    def doesVouch(self, _sender: Union[Account, Address], recipient: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#15)

        Args:
            _sender: address
            recipient: address
        Returns:
            bool
        """
        ...

    @overload
    def doesVouch(self, _sender: Union[Account, Address], recipient: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#15)

        Args:
            _sender: address
            recipient: address
        Returns:
            bool
        """
        ...

    @overload
    def doesVouch(self, _sender: Union[Account, Address], recipient: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#15)

        Args:
            _sender: address
            recipient: address
        Returns:
            bool
        """
        ...

    def doesVouch(self, _sender: Union[Account, Address], recipient: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#15)

        Args:
            _sender: address
            recipient: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "28da670a", [_sender, recipient], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

Vouch.generateVouchHash.selector = b'\xc4\xce\xeb\xb2'
Vouch.vouchFromSig.selector = b'4\x06\x1cp'
Vouch.lastUpdated.selector = b'\x06\x0e\xb2\xf5'
Vouch.vouchSender.selector = b'\xf6\xbb\x93\xec'
Vouch.vouchMsg.selector = b'1\xe1\xf5\xf7'
Vouch.userInfo.selector = b'\x19Y\xa0\x02'
Vouch.doesVouch.selector = b'(\xdag\n'
class VouchNFT(VouchDescriptor, ERC721S):
    """
    [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#19)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': '_vouch', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\xfc\xfd\xd1\x19': {'inputs': [], 'name': 'VOUCH_ID', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'approve', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x92\xb4\xc8\x1b': {'inputs': [{'components': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'description', 'type': 'string'}, {'internalType': 'string', 'name': 'image', 'type': 'string'}, {'internalType': 'string', 'name': 'attributes', 'type': 'string'}], 'internalType': 'struct NFTDescriptor.TokenURIParams', 'name': 'params', 'type': 'tuple'}], 'name': 'constructTokenURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'pure', 'type': 'function'}, b'x7\xab\xbe': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_lastUpdate', 'type': 'uint256'}, {'internalType': 'address', 'name': '_sender', 'type': 'address'}, {'internalType': 'string', 'name': '_msg', 'type': 'string'}], 'name': 'dataURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'0Mn-': {'inputs': [{'internalType': 'uint256', 'name': 'dayOfMonth', 'type': 'uint256'}], 'name': 'dayOfMonthString', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'pure', 'type': 'function'}, b'(\xdag\n': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}], 'name': 'doesVouch', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x17\xb7\xc8-': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'string', 'name': 'vouch', 'type': 'string'}], 'name': 'generateAttributesList', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb7\xd1h\xe6': {'inputs': [{'internalType': 'string', 'name': '_name', 'type': 'string'}, {'internalType': 'string', 'name': '_description', 'type': 'string'}, {'internalType': 'string', 'name': '_image', 'type': 'string'}, {'internalType': 'string', 'name': '_attributes', 'type': 'string'}], 'name': 'genericDataURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b' \xdd\xe5\xbd': {'inputs': [{'internalType': 'address', 'name': '_owner', 'type': 'address'}], 'name': 'getOwnerVouches', 'outputs': [{'internalType': 'bytes32[]', 'name': '', 'type': 'bytes32[]'}], 'stateMutability': 'view', 'type': 'function'}, b'J\x00\xde\xfe': {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'vouchId', 'type': 'bytes32'}], 'name': 'mintVouch', 'outputs': [{'internalType': 'bool', 'name': 'success', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8e6\xba\xad': {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'string', 'name': 'message', 'type': 'string'}, {'internalType': 'bytes', 'name': 'sig', 'type': 'bytes'}], 'name': 'mintVouchFromSig', 'outputs': [{'internalType': 'bool', 'name': 'success', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x0fL\x162': {'inputs': [{'internalType': 'uint256', 'name': 'month', 'type': 'uint256'}], 'name': 'monthStringShort', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'cR!\x1e': {'inputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'ownerOf', 'outputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'B\x84.\x0e': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb8\x8dO\xde': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa2,\xb4e': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'setApprovalForAll', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xdeQ\x01\xaf': {'inputs': [{'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'timestampToDate', 'outputs': [{'internalType': 'uint256', 'name': 'year', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'month', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'day', 'type': 'uint256'}], 'stateMutability': 'pure', 'type': 'function'}, b'X\x8a\x93\x88': {'inputs': [{'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'timestampToString', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'pure', 'type': 'function'}, b'qL\xffV': {'inputs': [], 'name': 'tokenIds', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xcc3\xc8u': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'tokenInfo', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc8{V\xdd': {'inputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'tokenURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'D@\xe8\xaf': {'inputs': [], 'name': 'vouch', 'outputs': [{'internalType': 'contract Vouch', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf9N\x92]': {'inputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'vouchToken', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}}
    _creation_code = "6080346200035557601f196001600160401b03601f6200278038819003828101851686018481118782101762000341578692829160405283396020958691810103126200035557516001600160a01b038116929083900362000355576200006562000359565b916009835268159bdd58da0813919560ba1b868401526200008562000359565b600595868252640ac9eaa86960db1b8883015284519084821162000341575f918254966001978881811c9116801562000336575b8c8210146200032257908b8288859411620002cc575b50508b90878311600114620002685785926200025c575b50505f19600383901b1c191690871b1782555b8251948511620002485785548681811c911680156200023d575b8a8210146200022957848111620001e3575b50889385116001146200017e57508394959697509262000172575b50505f19600383901b1c191690821b1790555b81546001600160a01b03191617905560405161240690816200037a8239f35b015190505f8062000140565b8493929193169785845280842093905b898210620001cb575050838596979810620001b2575b505050811b01905562000153565b01515f1960f88460031b161c191690555f8080620001a4565b8087859682949686015181550195019301906200018e565b868352898320858088018b1c8201928c89106200021f575b018a1c019087905b8281106200021357505062000125565b84815501879062000203565b92508192620001fb565b634e487b7160e01b83526022600452602483fd5b90607f169062000113565b634e487b7160e01b82526041600452602482fd5b015190505f80620000e6565b908c91858b95168780528388209388905b828210620002b2575050841162000299575b505050811b018255620000f9565b01515f1960f88460031b161c191690555f80806200028b565b8484015186558d9790950194938401939081019062000279565b9091925085805287828720918d828701901c830193861062000318575b918d8c928796959401901c01915b8281106200030957508d9150620000cf565b8781558594508b9101620002f7565b92508192620002e9565b634e487b7160e01b85526022600452602485fd5b90607f1690620000b9565b634e487b7160e01b5f52604160045260245ffd5b5f80fd5b60408051919082016001600160401b03811183821017620003415760405256fe60806040526004361015610011575f80fd5b5f3560e01c806301ffc9a7146101cf57806306fdde03146101ca578063095ea7b3146101c55780630f4c1632146101c057806317b7c82d146101bb57806320dde5bd146101b657806323b872dd146101a757806328da670a146101b1578063304d6e2d146101ac57806342842e0e146101a75780634440e8af146101a25780634a00defe1461019d578063588a9388146101985780636352211e1461019357806370a082311461018e578063714cff56146101895780637837abbe146101845780638e36baad1461017f57806392b4c81b1461017a57806395d89b4114610175578063a22cb46514610170578063b7d168e61461016b578063b88d4fde14610166578063c87b56dd14610161578063cc33c8751461015c578063de5101af14610157578063f94e925d146101525763fcfdd1191461014d575f80fd5b61100b565b610fe1565b610fb0565b610f86565b610df0565b610daa565b610d22565b610cfb565b610c32565b610b6f565b6109af565b610933565b610916565b610896565b610828565b610809565b610790565b610768565b610672565b610749565b610699565b610566565b6104ee565b61044f565b610433565b61031a565b3461023d57602036600319011261023d5760043563ffffffff60e01b811680910361023d576020906301ffc9a760e01b811490811561022c575b811561021b575b506040519015158152f35b635b5e139f60e01b1490505f610210565b6380ac58cd60e01b81149150610209565b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b61014081019081106001600160401b0382111761027157604052565b610241565b604081019081106001600160401b0382111761027157604052565b606081019081106001600160401b0382111761027157604052565b90601f801991011681019081106001600160401b0382111761027157604052565b5f5b8381106102de5750505f910152565b81810151838201526020016102cf565b6040916020825261030e81518092816020860152602086860191016102cd565b601f01601f1916010190565b3461023d575f8060031936011261041f57604051908080549060019180831c92808216928315610415575b60209283861085146104015785885260208801949081156103e05750600114610389575b61038587610379818903826102ac565b604051918291826102ee565b0390f35b5f805294509192917f290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e5635b8386106103cf5750505091019050610379826103855f80610369565b8054858701529482019481016103b3565b60ff191685525050505090151560051b019050610379826103855f80610369565b634e487b7160e01b82526022600452602482fd5b93607f1693610345565b80fd5b6001600160a01b0381160361023d57565b3461023d57604036600319011261023d5761023d600435610422565b3461023d57602036600319011261023d576103856103796004356118fe565b60405190608082018281106001600160401b0382111761027157604052565b6001600160401b03811161027157601f01601f191660200190565b81601f8201121561023d578035906104bf8261048d565b926104cd60405194856102ac565b8284526020838301011161023d57815f926020809301838601378301015290565b3461023d57604036600319011261023d576024356001600160401b03811161023d576103796105246103859236906004016104a8565b600435611602565b602090816040818301928281528551809452019301915f5b828110610552575050505090565b835185529381019392810192600101610544565b3461023d5760208060031936011261023d5760043561058481610422565b600554604051630cacd00160e11b81526001600160a01b0392831660048201525f929091839183916024918391165afa91821561066d5780926105d0575b60405180610385858261052c565b9091503d8082843e6105e281846102ac565b820190838383031261041f5782516001600160401b0393848211610669570182601f82011215610665578051938411610271578360051b916040519461062a878501876102ac565b8552858086019383010193841161041f57508401905b8282106106565750505061038591505f806105c2565b81518152908401908401610640565b5080fd5b8280fd5b6121f4565b3461023d57606036600319011261023d5761068e600435610422565b61023d602435610422565b3461023d57604036600319011261023d576004356106b681610422565b6020602435916106c583610422565b60055460405163146d338560e11b81526001600160a01b039283166004820152938216602485015283916044918391165afa801561066d57610385915f9161071b575b5060405190151581529081906020820190565b61073c915060203d8111610742575b61073481836102ac565b8101906121ff565b5f610708565b503d61072a565b3461023d57602036600319011261023d57610385610379600435611aad565b3461023d575f36600319011261023d576005546040516001600160a01b039091168152602090f35b3461023d57604036600319011261023d576004356107ad81610422565b6024355f81815260076020526040812054156107cf575b602060405160018152f35b6040916107f860045480956107e382611ba5565b60045581855260066020528386862055612248565b8152600760205220555f80806107c4565b3461023d57602036600319011261023d576103856103796004356116f7565b3461023d57602036600319011261023d576004355f908152600260205260409020546001600160a01b0316801561086457602090604051908152f35b60405162461bcd60e51b815260206004820152600a6024820152691393d517d3525395115160b21b6044820152606490fd5b3461023d57602036600319011261023d576004356108b381610422565b6001600160a01b031680156108e2575f52600360205261038560405f2054604051918291829190602083019252565b60405162461bcd60e51b815260206004820152600c60248201526b5a45524f5f4144445245535360a01b6044820152606490fd5b3461023d575f36600319011261023d576020600454604051908152f35b3461023d57608036600319011261023d5760443561095081610422565b6064356001600160401b03811161023d57610385916109766103799236906004016104a8565b90602435600435611193565b9181601f8401121561023d578235916001600160401b03831161023d576020838186019501011161023d57565b3461023d57606036600319011261023d57600480356109cd81610422565b6001600160401b039060243582811161023d576109ed9036908501610982565b9260443590811161023d57610a059036908601610982565b600554909390610a25906001600160a01b03165b6001600160a01b031690565b60405163626775d960e11b81526020979091889083908180610a4b8c8b8a8985016121d2565b03915afa91821561066d5788965f93610ab1928591610b42575b50610a78815f52600760205260405f2090565b5415610af8575b50600554610a95906001600160a01b0316610a19565b95604051998a988997889663034061c760e41b88528701612214565b03925af190811561066d57610385925f92610adb575b505060405190151581529081906020820190565b610af19250803d106107425761073481836102ac565b5f80610ac7565b610b3b845491610b0f610b0a84611ba5565b600455565b80610b22845f52600660205260405f2090565b55610b2d8389612248565b5f52600760205260405f2090565b555f610a7f565b610b629150893d8b11610b68575b610b5a81836102ac565b8101906121a3565b5f610a65565b503d610b50565b3461023d5760031960203682011261023d5760048035916001600160401b039081841161023d57608090843603011261023d57610baa61046e565b908383013581811161023d57610bc5908436918701016104a8565b8252602484013581811161023d57610be2908436918701016104a8565b6020830152604484013581811161023d57610c02908436918701016104a8565b6040830152606484013590811161023d576103859361037993610c2892369201016104a8565b606082015261105c565b3461023d575f8060031936011261041f576040519080600190815480831c92808216928315610ce7575b60209283861085146104015785885260208801949081156103e05750600114610c8f5761038587610379818903826102ac565b60015f5294509192917fb10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf65b838610610cd65750505091019050610379826103855f80610369565b805485870152948201948101610cba565b93607f1693610c5c565b8015150361023d57565b3461023d57604036600319011261023d57610d17600435610422565b61023d602435610cf1565b3461023d57608036600319011261023d576001600160401b0360043581811161023d57610d539036906004016104a8565b9060243581811161023d57610d6c9036906004016104a8565b9160443582811161023d57610d859036906004016104a8565b60643592831161023d5761038593610da46103799436906004016104a8565b926116bc565b3461023d57608036600319011261023d57610dc6600435610422565b610dd1602435610422565b6064356001600160401b03811161023d5761023d903690600401610982565b3461023d5760208060031936011261023d576005546004359190610e5390610e20906001600160a01b0316610a19565b82610e33855f52600660205260405f2090565b546040518094819263060eb2f560e01b8352600483019190602083019252565b0381845afa91821561066d575f92610f63575b50610e9e9083610e7e865f52600660205260405f2090565b5460405180948192633daee4fb60e21b8352600483019190602083019252565b0381845afa91821561066d57610eed945f93610f30575b50505f90610ecb865f52600660205260405f2090565b549060405180809781946331e1f5f760e01b8352600483019190602083019252565b03915afa91821561066d5761038594610379945f94610f0d575b50611193565b610f2991943d8091833e610f2181836102ac565b810190612372565b925f610f07565b5f9293509081610f5492903d10610f5c575b610f4c81836102ac565b81019061235d565b91905f610eb5565b503d610f42565b610e9e919250610f7f90843d8611610b6857610b5a81836102ac565b9190610e66565b3461023d57602036600319011261023d576004355f526006602052602060405f2054604051908152f35b3461023d57602036600319011261023d576060610fce600435611f4d565b9060405192835260208301526040820152f35b3461023d57602036600319011261023d576004355f526007602052602060405f2054604051908152f35b3461023d575f36600319011261023d5760206040517f2c74dac1fd3ae13388f7a55930dfea50b1d0adc16bacffd74160c1dd2170b2828152f35b90611058602092828151948592016102cd565b0190565b6111906110b861114f6111849361113661112882519261110461110a602083015192611104603b606060408401519301519560296040519c8d809c683d913730b6b2911d1160b91b6020830152602081519485930191016102cd565b8a0171111610113232b9b1b934b83a34b7b7111d1160711b60298201526110e882518093602086850191016102cd565b0101600d906c1116101134b6b0b3b2911d101160991b81520190565b90611045565b71222c202261747472696275746573223a205b60701b815260120190565b615d7d60f01b815260020190565b039161114a601f19938481018352826102ac565b611e5b565b6040517f646174613a6170706c69636174696f6e2f6a736f6e3b6261736536342c0000006020820152938491603d8301611104565b039081018352826102ac565b90565b929190926111a081611c4d565b926040928351958660209687820166566f756368202360c81b90528051908189602785019201916111d0926102cd565b8101036007810188526027016111e690886102ac565b8451906111f282610255565b61010282527f3c73766720786d6c6e733d22687474703a2f2f7777772e77332e6f72672f3230878301527f30302f73766722207072657365727665417370656374526174696f3d22784d69868301527f6e594d696e206d656574222076696577426f783d22302030203335302033353060608301527f223e3c7374796c653e2e62617365207b2066696c6c3a20233030343434303b2060808301527f666f6e742d66616d696c793a2073657269663b20666f6e742d73697a653a203160a08301527f3570783b207d3c2f7374796c653e3c726563742077696474683d22313030252260c08301527f206865696768743d2231303025222066696c6c3d222365656535643322202f3e60e08301527f3c7465787420783d223235302220793d2234302220636c6173733d226261736561010083015261111f60f11b61012083015261133b906116f7565b90855191829188830161134d91611045565b61135691611045565b7f3c2f746578743e3c7465787420783d2232302220793d2238302220636c6173738152671e913130b9b2911f60c11b60208201526028010391601f199283810183526113a290836102ac565b855180928882016113b291611045565b6113bc9086611045565b7f3c2f746578743e3c7465787420783d2232302220793d223236352220636c617381527f733d2262617365223e66726f6d3a203c2f746578743e3c7465787420783d223260208201527f302220793d223239302220636c6173733d2262617365223e0000000000000000604082015260580103838101835261143e90836102ac565b61144790611cea565b9061145185611c4d565b865192839289840161146291611045565b61146b91611045565b7f3c2f746578743e3c7465787420783d223234302220793d223333302220636c61815271039b99e913130b9b2911f3b37bab1b41011960751b60208201526032016114b591611045565b6c1e17ba32bc3a1f1e17b9bb339f60991b8152600d010382810182526114db90826102ac565b6114e490611e5b565b938051809587820161151a90601a907f646174613a696d6167652f7376672b786d6c3b6261736536342c00000000000081520190565b61152391611045565b03828101865261153390866102ac565b51809581016115bd906062907f54686973204e465420726570726573656e74732061207369676e6564206d657381527f736167652066726f6d20612073656e64657220746f207468697320616464726560208201527f73732e2054686973204e46542063616e6e6f74206265207472616e7366657265604082015261321760f11b60608201520190565b0390810185526115cd90856102ac565b6115d691611602565b91611190936116bc565b60405190602082018281106001600160401b03821117610271576040525f8252565b606461161061119092611c4d565b926040519384917f7b2274726169745f74797065223a22566f756368222c2276616c7565223a22006020840152611651815180926020603f870191016102cd565b820162089f4b60ea1b603f8201527f7b2274726169745f74797065223a22566f756368204944222c2276616c7565226042820152601d60f91b60628201526116a38251809360206063850191016102cd565b01607d60f81b60638201520360448101845201826102ac565b9290916040519260808401948486106001600160401b038711176102715761119095604052845260208401526040830152606082015261105c565b611190602261171961172561170e61171f95611f4d565b969196939093611aad565b926118fe565b94611c4d565b604051948261173e8794518092602080880191016102cd565b830190600160fd1b918260208201526117618251809360206021850191016102cd565b0190602182015261177b82518093602087850191016102cd565b010360028101845201826102ac565b6040519061179782610276565b60038252622530b760e91b6020830152565b604051906117b682610276565b60038252622332b160e91b6020830152565b604051906117d582610276565b600382526226b0b960e91b6020830152565b604051906117f482610276565b600382526220b83960e91b6020830152565b6040519061181382610276565b60038252624d617960e81b6020830152565b6040519061183282610276565b6003825262253ab760e91b6020830152565b6040519061185182610276565b6003825262129d5b60ea1b6020830152565b6040519061187082610276565b600382526241756760e81b6020830152565b6040519061188f82610276565b600382526205365760ec1b6020830152565b604051906118ae82610276565b600382526213d8dd60ea1b6020830152565b604051906118cd82610276565b60038252622737bb60e91b6020830152565b604051906118ec82610276565b600382526244656360e81b6020830152565b600181146119c757600281146119be57600381146119b557600481146119ac57600581146119a3576006811461199a57600781146119915760088114611988576009811461197f57600a811461197657600b811461196d57600c14611965576111906115e0565b6111906118df565b506111906118c0565b506111906118a1565b50611190611882565b50611190611863565b50611190611844565b50611190611825565b50611190611806565b506111906117e7565b506111906117c8565b506111906117a9565b5061119061178a565b604051906119dd82610276565b60038252620c5cdd60ea1b6020830152565b604051906119fc82610276565b60038252620c9b9960ea1b6020830152565b60405190611a1b82610276565b60038252620cdc9960ea1b6020830152565b60405190611a3a82610276565b60048252630c8c5cdd60e21b6020830152565b60405190611a5a82610276565b60048252630c8c9b9960e21b6020830152565b60405190611a7a82610276565b60048252630c8cdc9960e21b6020830152565b60405190611a9a82610276565b60048252630ccc5cdd60e21b6020830152565b9060609160018114611b865760028114611b7b5760038114611b705760158114611b655760168114611b5a5760178114611b4f57601f8114611b4457601f811080611b3b575b611afa5750565b611b1f919250611b0c61119091611c4d565b611b2d6040519384926020840190611045565b610e8d60f31b815260020190565b03601f1981018352826102ac565b50801515611af3565b509050611190611a8d565b509050611190611a6d565b509050611190611a4d565b509050611190611a2d565b509050611190611a0e565b5090506111906119ef565b5090506111906119d0565b634e487b7160e01b5f52601160045260245ffd5b5f198114611bb35760010190565b611b91565b90611bc28261048d565b611bcf60405191826102ac565b8281528092611be0601f199161048d565b0190602036910137565b9060028201809211611bb357565b9060208201809211611bb357565b634e487b7160e01b5f52603260045260245ffd5b805115611c275760200190565b611c06565b805160011015611c275760210190565b908151811015611c27570160200190565b8015611ccc57805f8082805b611cb45750611c6781611bb8565b935b611c735750505090565b5f198101908111611bb3578092600a9160308383068101809111611bb35760f81b6001600160f81b031916841a90611cab9087611c3c565b53049182611c69565b9250611cc1600a91611ba5565b920480849391611c59565b50604051611cd981610276565b60018152600360fc1b602082015290565b604051906001600160a01b0316611d0082610291565b602a825260403660208401376030611d1783611c1a565b536078611d2383611c2c565b536029905b60018211611d3b57611190915015611da1565b600f8116906010821015611c2757611d77916f181899199a1a9b1b9c1cb0b131b232b360811b901a611d6d8486611c3c565b5360041c91611d95565b90611d28565b600281901b91906001600160fe1b03811603611bb357565b8015611bb3575f190190565b15611da857565b606460405162461bcd60e51b815260206004820152602060248201527f537472696e67733a20686578206c656e67746820696e73756666696369656e746044820152fd5b60405190606082018281106001600160401b0382111761027157604052604082527f6768696a6b6c6d6e6f707172737475767778797a303132333435363738392b2f6040837f4142434445464748494a4b4c4d4e4f505152535455565758595a61626364656660208201520152565b805115611f4457611e6a611dec565b611e86611e81611e7a8451611bea565b6003900490565b611d7d565b91611e98611e9384611bf8565b611bb8565b92835280815182019060208501935b828210611ee857505050600390510680600114611ed757600214611ec9575090565b603d60f81b5f199091015290565b50613d3d60f01b6001199091015290565b90919360049060038094019384516001603f81818460121c16880101519260f893841b8652828282600c1c1689010151841b8387015282828260061c1689010151841b60028701521686010151901b9082015201939190611ea7565b506111906115e0565b62015180900462010bd9908181019182125f8212908015821691151617611bb3576226496501905f62253d8c83129112908015821691151617611bb357611fc4611fa2611f99836120ec565b62023ab1900590565b91611fbe611fb7611fb2856120fd565b612061565b6004900590565b9061218b565b9061205b611ffd611ff8611feb611fe2611fdd8761207d565b612110565b62164b09900590565b94611fbe611fb787612122565b612099565b61205661202b61201761200f84612134565b61098f900590565b92611fbe61202485612145565b6050900590565b9461205661205161204b612042600b8705966120b5565b611fbe87612157565b96612179565b612168565b6120d1565b91909192565b9060038201915f600384129112908015821691151617611bb357565b9060018201915f600184129112908015821691151617611bb357565b90601f8201915f601f84129112908015821691151617611bb357565b9060028201915f600284129112908015821691151617611bb357565b9190915f8382019384129112908015821691151617611bb357565b908160021b916004830503611bb357565b9062023ab19180830292830503611bb357565b90610fa09180830292830503611bb357565b906105b59180830292830503611bb357565b9081605002916050830503611bb357565b9061098f9180830292830503611bb357565b9081600c0291600c830503611bb357565b9081606402916064830503611bb357565b906030198201918213600116611bb357565b81810392915f138015828513169184121617611bb357565b9081602091031261023d575190565b908060209392818452848401375f828201840152601f01601f1916010190565b6001600160a01b039091168152604060208201819052611190939101916121b2565b6040513d5f823e3d90fd5b9081602091031261023d575161119081610cf1565b9391611190959361223a9260018060a01b031686526060602087015260608601916121b2565b9260408185039101526121b2565b6001600160a01b03818116919082156123245761226d845f52600260205260405f2090565b54166122ee576001600160a01b0381165f9081526003602052604090206122c79190805460010190556122a8845f52600260205260405f2090565b80546001600160a01b0319166001600160a01b03909216919091179055565b5f7fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef8180a4565b60405162461bcd60e51b815260206004820152600e60248201526d1053149150511657d3525395115160921b6044820152606490fd5b60405162461bcd60e51b81526020600482015260116024820152701253959053125117d49150d25412515395607a1b6044820152606490fd5b9081602091031261023d575161119081610422565b60208183031261023d578051906001600160401b03821161023d570181601f8201121561023d5780516123a48161048d565b926123b260405194856102ac565b8184526020828401011161023d5761119091602080850191016102cd56fea2646970667358221220311f239afe2c904ed98999a60b8b95aca658b11f0ee40412eb2af6038d0c81bd64736f6c63430008140033"

    @overload
    @classmethod
    def deploy(cls, _vouch: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#31)

        Args:
            _vouch: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _vouch: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> VouchNFT:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#31)

        Args:
            _vouch: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _vouch: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#31)

        Args:
            _vouch: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _vouch: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#31)

        Args:
            _vouch: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _vouch: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[VouchNFT]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#31)

        Args:
            _vouch: address
        """
        ...

    @classmethod
    def deploy(cls, _vouch: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, VouchNFT, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[VouchNFT]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#31)

        Args:
            _vouch: address
        """
        return cls._deploy(request_type, [_vouch], return_tx, VouchNFT, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def VOUCH_ID(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#24)

        Returns:
            bytes32
        """
        ...

    @overload
    def VOUCH_ID(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#24)

        Returns:
            bytes32
        """
        ...

    @overload
    def VOUCH_ID(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#24)

        Returns:
            bytes32
        """
        ...

    @overload
    def VOUCH_ID(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#24)

        Returns:
            bytes32
        """
        ...

    def VOUCH_ID(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#24)

        Returns:
            bytes32
        """
        return self._execute(self.chain, request_type, "fcfdd119", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tokenIds(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#25)

        Returns:
            uint256
        """
        ...

    @overload
    def tokenIds(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#25)

        Returns:
            uint256
        """
        ...

    @overload
    def tokenIds(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#25)

        Returns:
            uint256
        """
        ...

    @overload
    def tokenIds(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#25)

        Returns:
            uint256
        """
        ...

    def tokenIds(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#25)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "714cff56", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def vouch(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Vouch:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#26)

        Returns:
            contract Vouch
        """
        ...

    @overload
    def vouch(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#26)

        Returns:
            contract Vouch
        """
        ...

    @overload
    def vouch(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#26)

        Returns:
            contract Vouch
        """
        ...

    @overload
    def vouch(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Vouch]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#26)

        Returns:
            contract Vouch
        """
        ...

    def vouch(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Vouch, TransactionAbc[Vouch], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#26)

        Returns:
            contract Vouch
        """
        return self._execute(self.chain, request_type, "4440e8af", [], True if request_type == "tx" else False, Vouch, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tokenInfo(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#28)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def tokenInfo(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#28)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def tokenInfo(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#28)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def tokenInfo(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#28)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    def tokenInfo(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#28)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        return self._execute(self.chain, request_type, "cc33c875", [key0], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def vouchToken(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#29)

        Args:
            key0: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def vouchToken(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#29)

        Args:
            key0: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def vouchToken(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#29)

        Args:
            key0: bytes32
        Returns:
            uint256
        """
        ...

    @overload
    def vouchToken(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#29)

        Args:
            key0: bytes32
        Returns:
            uint256
        """
        ...

    def vouchToken(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#29)

        Args:
            key0: bytes32
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "f94e925d", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def mintVouchFromSig(self, recipient: Union[Account, Address], message: str, sig: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#41)

        Args:
            recipient: address
            message: string
            sig: bytes
        Returns:
            bool
        """
        ...

    @overload
    def mintVouchFromSig(self, recipient: Union[Account, Address], message: str, sig: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#41)

        Args:
            recipient: address
            message: string
            sig: bytes
        Returns:
            bool
        """
        ...

    @overload
    def mintVouchFromSig(self, recipient: Union[Account, Address], message: str, sig: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#41)

        Args:
            recipient: address
            message: string
            sig: bytes
        Returns:
            bool
        """
        ...

    @overload
    def mintVouchFromSig(self, recipient: Union[Account, Address], message: str, sig: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#41)

        Args:
            recipient: address
            message: string
            sig: bytes
        Returns:
            bool
        """
        ...

    def mintVouchFromSig(self, recipient: Union[Account, Address], message: str, sig: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#41)

        Args:
            recipient: address
            message: string
            sig: bytes
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "8e36baad", [recipient, message, sig], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def mintVouch(self, recipient: Union[Account, Address], vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#57)

        Args:
            recipient: address
            vouchId: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def mintVouch(self, recipient: Union[Account, Address], vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#57)

        Args:
            recipient: address
            vouchId: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def mintVouch(self, recipient: Union[Account, Address], vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#57)

        Args:
            recipient: address
            vouchId: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def mintVouch(self, recipient: Union[Account, Address], vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#57)

        Args:
            recipient: address
            vouchId: bytes32
        Returns:
            bool
        """
        ...

    def mintVouch(self, recipient: Union[Account, Address], vouchId: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#57)

        Args:
            recipient: address
            vouchId: bytes32
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "4a00defe", [recipient, vouchId], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tokenURI(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#75)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def tokenURI(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#75)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def tokenURI(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#75)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def tokenURI(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#75)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    def tokenURI(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#75)

        Args:
            id: uint256
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "c87b56dd", [id], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getOwnerVouches(self, _owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[bytes32]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#84)

        Args:
            _owner: address
        Returns:
            bytes32[]
        """
        ...

    @overload
    def getOwnerVouches(self, _owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#84)

        Args:
            _owner: address
        Returns:
            bytes32[]
        """
        ...

    @overload
    def getOwnerVouches(self, _owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#84)

        Args:
            _owner: address
        Returns:
            bytes32[]
        """
        ...

    @overload
    def getOwnerVouches(self, _owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[bytes32]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#84)

        Args:
            _owner: address
        Returns:
            bytes32[]
        """
        ...

    def getOwnerVouches(self, _owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[bytes32], TransactionAbc[List[bytes32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#84)

        Args:
            _owner: address
        Returns:
            bytes32[]
        """
        return self._execute(self.chain, request_type, "20dde5bd", [_owner], True if request_type == "tx" else False, List[bytes32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def doesVouch(self, sender: Union[Account, Address], recipient: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#89)

        Args:
            sender: address
            recipient: address
        Returns:
            bool
        """
        ...

    @overload
    def doesVouch(self, sender: Union[Account, Address], recipient: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#89)

        Args:
            sender: address
            recipient: address
        Returns:
            bool
        """
        ...

    @overload
    def doesVouch(self, sender: Union[Account, Address], recipient: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#89)

        Args:
            sender: address
            recipient: address
        Returns:
            bool
        """
        ...

    @overload
    def doesVouch(self, sender: Union[Account, Address], recipient: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#89)

        Args:
            sender: address
            recipient: address
        Returns:
            bool
        """
        ...

    def doesVouch(self, sender: Union[Account, Address], recipient: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/VouchNFT.sol#89)

        Args:
            sender: address
            recipient: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "28da670a", [sender, recipient], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

VouchNFT.VOUCH_ID.selector = b'\xfc\xfd\xd1\x19'
VouchNFT.tokenIds.selector = b'qL\xffV'
VouchNFT.vouch.selector = b'D@\xe8\xaf'
VouchNFT.tokenInfo.selector = b'\xcc3\xc8u'
VouchNFT.vouchToken.selector = b'\xf9N\x92]'
VouchNFT.mintVouchFromSig.selector = b'\x8e6\xba\xad'
VouchNFT.mintVouch.selector = b'J\x00\xde\xfe'
VouchNFT.tokenURI.selector = b'\xc8{V\xdd'
VouchNFT.getOwnerVouches.selector = b' \xdd\xe5\xbd'
VouchNFT.doesVouch.selector = b'(\xdag\n'
