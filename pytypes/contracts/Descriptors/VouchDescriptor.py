
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from woke.development.core import Contract, Library, Address, Account, Chain, RequestType
from woke.development.primitive_types import *
from woke.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.contracts.Descriptors.NFTDescriptor import NFTDescriptor



class VouchDescriptor(NFTDescriptor):
    """
    [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#10)
    """
    _abi = {b'\x92\xb4\xc8\x1b': {'inputs': [{'components': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'description', 'type': 'string'}, {'internalType': 'string', 'name': 'image', 'type': 'string'}, {'internalType': 'string', 'name': 'attributes', 'type': 'string'}], 'internalType': 'struct NFTDescriptor.TokenURIParams', 'name': 'params', 'type': 'tuple'}], 'name': 'constructTokenURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'pure', 'type': 'function'}, b'x7\xab\xbe': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_lastUpdate', 'type': 'uint256'}, {'internalType': 'address', 'name': '_sender', 'type': 'address'}, {'internalType': 'string', 'name': '_msg', 'type': 'string'}], 'name': 'dataURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'0Mn-': {'inputs': [{'internalType': 'uint256', 'name': 'dayOfMonth', 'type': 'uint256'}], 'name': 'dayOfMonthString', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x17\xb7\xc8-': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'string', 'name': 'vouch', 'type': 'string'}], 'name': 'generateAttributesList', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb7\xd1h\xe6': {'inputs': [{'internalType': 'string', 'name': '_name', 'type': 'string'}, {'internalType': 'string', 'name': '_description', 'type': 'string'}, {'internalType': 'string', 'name': '_image', 'type': 'string'}, {'internalType': 'string', 'name': '_attributes', 'type': 'string'}], 'name': 'genericDataURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x0fL\x162': {'inputs': [{'internalType': 'uint256', 'name': 'month', 'type': 'uint256'}], 'name': 'monthStringShort', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xdeQ\x01\xaf': {'inputs': [{'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'timestampToDate', 'outputs': [{'internalType': 'uint256', 'name': 'year', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'month', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'day', 'type': 'uint256'}], 'stateMutability': 'pure', 'type': 'function'}, b'X\x8a\x93\x88': {'inputs': [{'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'timestampToString', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'pure', 'type': 'function'}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> VouchDescriptor:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[VouchDescriptor]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, VouchDescriptor, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[VouchDescriptor]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @overload
    def dataURI(self, tokenId: uint256, _lastUpdate: uint256, _sender: Union[Account, Address], _msg: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#24)

        Args:
            tokenId: uint256
            _lastUpdate: uint256
            _sender: address
            _msg: string
        Returns:
            string
        """
        ...

    @overload
    def dataURI(self, tokenId: uint256, _lastUpdate: uint256, _sender: Union[Account, Address], _msg: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#24)

        Args:
            tokenId: uint256
            _lastUpdate: uint256
            _sender: address
            _msg: string
        Returns:
            string
        """
        ...

    @overload
    def dataURI(self, tokenId: uint256, _lastUpdate: uint256, _sender: Union[Account, Address], _msg: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#24)

        Args:
            tokenId: uint256
            _lastUpdate: uint256
            _sender: address
            _msg: string
        Returns:
            string
        """
        ...

    @overload
    def dataURI(self, tokenId: uint256, _lastUpdate: uint256, _sender: Union[Account, Address], _msg: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#24)

        Args:
            tokenId: uint256
            _lastUpdate: uint256
            _sender: address
            _msg: string
        Returns:
            string
        """
        ...

    def dataURI(self, tokenId: uint256, _lastUpdate: uint256, _sender: Union[Account, Address], _msg: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#24)

        Args:
            tokenId: uint256
            _lastUpdate: uint256
            _sender: address
            _msg: string
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "7837abbe", [tokenId, _lastUpdate, _sender, _msg], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def generateAttributesList(self, tokenId: uint256, vouch: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#47)

        Args:
            tokenId: uint256
            vouch: string
        Returns:
            string
        """
        ...

    @overload
    def generateAttributesList(self, tokenId: uint256, vouch: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#47)

        Args:
            tokenId: uint256
            vouch: string
        Returns:
            string
        """
        ...

    @overload
    def generateAttributesList(self, tokenId: uint256, vouch: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#47)

        Args:
            tokenId: uint256
            vouch: string
        Returns:
            string
        """
        ...

    @overload
    def generateAttributesList(self, tokenId: uint256, vouch: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#47)

        Args:
            tokenId: uint256
            vouch: string
        Returns:
            string
        """
        ...

    def generateAttributesList(self, tokenId: uint256, vouch: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#47)

        Args:
            tokenId: uint256
            vouch: string
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "17b7c82d", [tokenId, vouch], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def genericDataURI(self, _name: str, _description: str, _image: str, _attributes: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#59)

        Args:
            _name: string
            _description: string
            _image: string
            _attributes: string
        Returns:
            string
        """
        ...

    @overload
    def genericDataURI(self, _name: str, _description: str, _image: str, _attributes: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#59)

        Args:
            _name: string
            _description: string
            _image: string
            _attributes: string
        Returns:
            string
        """
        ...

    @overload
    def genericDataURI(self, _name: str, _description: str, _image: str, _attributes: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#59)

        Args:
            _name: string
            _description: string
            _image: string
            _attributes: string
        Returns:
            string
        """
        ...

    @overload
    def genericDataURI(self, _name: str, _description: str, _image: str, _attributes: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#59)

        Args:
            _name: string
            _description: string
            _image: string
            _attributes: string
        Returns:
            string
        """
        ...

    def genericDataURI(self, _name: str, _description: str, _image: str, _attributes: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#59)

        Args:
            _name: string
            _description: string
            _image: string
            _attributes: string
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "b7d168e6", [_name, _description, _image, _attributes], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def timestampToDate(self, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[uint256, uint256, uint256]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#74)

        Args:
            timestamp: uint256
        Returns:
            (uint256, uint256, uint256)
        """
        ...

    @overload
    def timestampToDate(self, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#74)

        Args:
            timestamp: uint256
        Returns:
            (uint256, uint256, uint256)
        """
        ...

    @overload
    def timestampToDate(self, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#74)

        Args:
            timestamp: uint256
        Returns:
            (uint256, uint256, uint256)
        """
        ...

    @overload
    def timestampToDate(self, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[uint256, uint256, uint256]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#74)

        Args:
            timestamp: uint256
        Returns:
            (uint256, uint256, uint256)
        """
        ...

    def timestampToDate(self, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[uint256, uint256, uint256], TransactionAbc[Tuple[uint256, uint256, uint256]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#74)

        Args:
            timestamp: uint256
        Returns:
            (uint256, uint256, uint256)
        """
        return self._execute(self.chain, request_type, "de5101af", [timestamp], True if request_type == "tx" else False, Tuple[uint256, uint256, uint256], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def timestampToString(self, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#78)

        Args:
            timestamp: uint256
        Returns:
            string
        """
        ...

    @overload
    def timestampToString(self, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#78)

        Args:
            timestamp: uint256
        Returns:
            string
        """
        ...

    @overload
    def timestampToString(self, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#78)

        Args:
            timestamp: uint256
        Returns:
            string
        """
        ...

    @overload
    def timestampToString(self, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#78)

        Args:
            timestamp: uint256
        Returns:
            string
        """
        ...

    def timestampToString(self, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#78)

        Args:
            timestamp: uint256
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "588a9388", [timestamp], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def monthStringShort(self, month: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#83)

        Args:
            month: uint256
        Returns:
            string
        """
        ...

    @overload
    def monthStringShort(self, month: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#83)

        Args:
            month: uint256
        Returns:
            string
        """
        ...

    @overload
    def monthStringShort(self, month: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#83)

        Args:
            month: uint256
        Returns:
            string
        """
        ...

    @overload
    def monthStringShort(self, month: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#83)

        Args:
            month: uint256
        Returns:
            string
        """
        ...

    def monthStringShort(self, month: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#83)

        Args:
            month: uint256
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "0f4c1632", [month], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def dayOfMonthString(self, dayOfMonth: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#99)

        Args:
            dayOfMonth: uint256
        Returns:
            string
        """
        ...

    @overload
    def dayOfMonthString(self, dayOfMonth: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#99)

        Args:
            dayOfMonth: uint256
        Returns:
            string
        """
        ...

    @overload
    def dayOfMonthString(self, dayOfMonth: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#99)

        Args:
            dayOfMonth: uint256
        Returns:
            string
        """
        ...

    @overload
    def dayOfMonthString(self, dayOfMonth: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#99)

        Args:
            dayOfMonth: uint256
        Returns:
            string
        """
        ...

    def dayOfMonthString(self, dayOfMonth: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/VouchDescriptor.sol#99)

        Args:
            dayOfMonth: uint256
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "304d6e2d", [dayOfMonth], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

VouchDescriptor.dataURI.selector = b'x7\xab\xbe'
VouchDescriptor.generateAttributesList.selector = b'\x17\xb7\xc8-'
VouchDescriptor.genericDataURI.selector = b'\xb7\xd1h\xe6'
VouchDescriptor.timestampToDate.selector = b'\xdeQ\x01\xaf'
VouchDescriptor.timestampToString.selector = b'X\x8a\x93\x88'
VouchDescriptor.monthStringShort.selector = b'\x0fL\x162'
VouchDescriptor.dayOfMonthString.selector = b'0Mn-'
