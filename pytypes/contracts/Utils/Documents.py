
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from woke.development.core import Contract, Library, Address, Account, Chain, RequestType
from woke.development.primitive_types import *
from woke.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class Documents(Contract):
    """
    [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#9)
    """
    _abi = {b'\x9f\xa5\xf5\x0b': {'inputs': [], 'name': 'getAllDocuments', 'outputs': [{'internalType': 'string[]', 'name': '', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'|\xcbjd': {'inputs': [{'internalType': 'string', 'name': '_name', 'type': 'string'}], 'name': 'getDocument', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}, {'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'=\x1c"s': {'inputs': [], 'name': 'getDocumentCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc6\xb5G\xe6': {'inputs': [{'internalType': 'uint256', 'name': '_index', 'type': 'uint256'}], 'name': 'getDocumentName', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}}
    _creation_code = "60808060405234610016576103fd908161001b8239f35b5f80fdfe608060408181526004361015610013575f80fd5b5f91823560e01c9081633d1c227314610269575080637ccb6a64146101be5780639fa5f50b146100ba5763c6b547e61461004b575f80fd5b346100b65760203660031901126100b6576004356002548110156100b25761009b9060026100ae94527f405787fa12a823e0f2b7631cc41b3ba8828b3321ca811111fa75cd3aa3bb5ace016102f9565b9051918291602083526020830190610285565b0390f35b8280fd5b5080fd5b5090346101bb57806003193601126101bb5760025467ffffffffffffffff81116101a7578251916020926100f3848460051b01826102c3565b8281526002825283810192827f405787fa12a823e0f2b7631cc41b3ba8828b3321ca811111fa75cd3aa3bb5ace855b83831061018357505050508451938085019181865251809252858501958260051b8601019392955b8287106101575785850386f35b909192938280610173600193603f198a82030186528851610285565b960192019601959291909261014a565b6001888192610195859b98999b6102f9565b81520192019201919096949396610122565b634e487b7160e01b82526041600452602482fd5b80fd5b50346100b65760203660031901126100b65760043567ffffffffffffffff8082116102655736602383011215610265578160040135818111610261576024830192602482369201011161026157602061024393600186518483823783818681018b815203019020019683875194859384378201908152030190205460201c16926102f9565b916102578251938385948552840190610285565b9060208301520390f35b8480fd5b8380fd5b8390346100b657816003193601126100b6576020906002548152f35b91908251928382525f5b8481106102af575050825f602080949584010152601f8019910116010190565b60208183018101518483018201520161028f565b90601f8019910116810190811067ffffffffffffffff8211176102e557604052565b634e487b7160e01b5f52604160045260245ffd5b90604051905f835490600182811c908084169687156103bd575b60209485841089146103a957879884899798995290815f146103875750600114610349575b505050610347925003836102c3565b565b5f90815285812095935091905b81831061036f57505061034793508201015f8080610338565b85548884018501529485019487945091830191610356565b9250505061034794925060ff191682840152151560051b8201015f8080610338565b634e487b7160e01b85526022600452602485fd5b91607f169161031356fea2646970667358221220b8ee57cb733781698ed99411a6823a0cfe20a0bdd776a4442e3098372ee037d564736f6c63430008140033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Documents:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Documents]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, Documents, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[Documents]]:
        return cls._deploy(request_type, [], return_tx, Documents, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class Document:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#11)

        Attributes:
            docIndex (uint32): uint32
            lastModified (uint64): uint64
            data (str): string
        """
        original_name = 'Document'

        docIndex: uint32
        lastModified: uint64
        data: str


    @dataclasses.dataclass
    class DocumentRemoved:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#25)

        Attributes:
            _name_hash (bytes): indexed string
            _data (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'string', 'name': '_name', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': '_data', 'type': 'string'}], 'name': 'DocumentRemoved', 'type': 'event'}
        original_name = 'DocumentRemoved'
        selector = b'KS8T\x0bM\x1c\x0fm\xd00\x8a%\xf63\xb7\xff`G/\x89Mq\x1c\xff\x9d\xd6N5\xc6\x13\xb2'

        _name_hash: bytes = dataclasses.field(metadata={"original_name": "_name"})
        _data: str


    @dataclasses.dataclass
    class DocumentUpdated:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#26)

        Attributes:
            _name_hash (bytes): indexed string
            _data (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'string', 'name': '_name', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': '_data', 'type': 'string'}], 'name': 'DocumentUpdated', 'type': 'event'}
        original_name = 'DocumentUpdated'
        selector = b'\xba\xa2\x06\xe5\xea\x80\x0e\xb8\x8b\xce\t\x9fE?\xeeS)[y;\x9d]\x1c\xfcL\xe4\xb6\xdb\x06\xa3OS'

        _name_hash: bytes = dataclasses.field(metadata={"original_name": "_name"})
        _data: str


    @overload
    def getDocument(self, _name: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[str, uint256]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#70)

        Args:
            _name: string
        Returns:
            (string, uint256)
        """
        ...

    @overload
    def getDocument(self, _name: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#70)

        Args:
            _name: string
        Returns:
            (string, uint256)
        """
        ...

    @overload
    def getDocument(self, _name: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#70)

        Args:
            _name: string
        Returns:
            (string, uint256)
        """
        ...

    @overload
    def getDocument(self, _name: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[str, uint256]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#70)

        Args:
            _name: string
        Returns:
            (string, uint256)
        """
        ...

    def getDocument(self, _name: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[str, uint256], TransactionAbc[Tuple[str, uint256]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#70)

        Args:
            _name: string
        Returns:
            (string, uint256)
        """
        return self._execute(self.chain, request_type, "7ccb6a64", [_name], True if request_type == "tx" else False, Tuple[str, uint256], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getAllDocuments(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#81)

        Returns:
            string[]
        """
        ...

    @overload
    def getAllDocuments(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#81)

        Returns:
            string[]
        """
        ...

    @overload
    def getAllDocuments(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#81)

        Returns:
            string[]
        """
        ...

    @overload
    def getAllDocuments(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[str]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#81)

        Returns:
            string[]
        """
        ...

    def getAllDocuments(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[str], TransactionAbc[List[str]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#81)

        Returns:
            string[]
        """
        return self._execute(self.chain, request_type, "9fa5f50b", [], True if request_type == "tx" else False, List[str], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getDocumentCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#89)

        Returns:
            uint256
        """
        ...

    @overload
    def getDocumentCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#89)

        Returns:
            uint256
        """
        ...

    @overload
    def getDocumentCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#89)

        Returns:
            uint256
        """
        ...

    @overload
    def getDocumentCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#89)

        Returns:
            uint256
        """
        ...

    def getDocumentCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#89)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "3d1c2273", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getDocumentName(self, _index: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#97)

        Args:
            _index: uint256
        Returns:
            string
        """
        ...

    @overload
    def getDocumentName(self, _index: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#97)

        Args:
            _index: uint256
        Returns:
            string
        """
        ...

    @overload
    def getDocumentName(self, _index: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#97)

        Args:
            _index: uint256
        Returns:
            string
        """
        ...

    @overload
    def getDocumentName(self, _index: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#97)

        Args:
            _index: uint256
        Returns:
            string
        """
        ...

    def getDocumentName(self, _index: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Utils/Documents.sol#97)

        Args:
            _index: uint256
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "c6b547e6", [_index], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

Documents.getDocument.selector = b'|\xcbjd'
Documents.getAllDocuments.selector = b'\x9f\xa5\xf5\x0b'
Documents.getDocumentCount.selector = b'=\x1c"s'
Documents.getDocumentName.selector = b'\xc6\xb5G\xe6'
