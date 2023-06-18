
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from woke.development.core import Contract, Library, Address, Account, Chain, RequestType
from woke.development.primitive_types import *
from woke.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class NFTDescriptor(Contract):
    """
    [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/NFTDescriptor.sol#9)
    """
    _abi = {b'\x92\xb4\xc8\x1b': {'inputs': [{'components': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'description', 'type': 'string'}, {'internalType': 'string', 'name': 'image', 'type': 'string'}, {'internalType': 'string', 'name': 'attributes', 'type': 'string'}], 'internalType': 'struct NFTDescriptor.TokenURIParams', 'name': 'params', 'type': 'tuple'}], 'name': 'constructTokenURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'pure', 'type': 'function'}}
    _creation_code = "60808060405234610016576105a3908161001b8239f35b5f80fdfe6080604052600480361015610012575f80fd5b5f90813560e01c6392b4c81b14610027575f80fd5b346100fd57600319906020368301126101095780359167ffffffffffffffff9081841161010557608090843603011261010157610062610148565b93838301358281116100fd5761007d90843691870101610184565b855260248401358281116100fd5761009a90843691870101610184565b602086015260448401358281116100fd576100ba90843691870101610184565b604086015260648401359182116100fa576100f66100ea866100e0368689018801610184565b6060820152610232565b604051918291826101ef565b0390f35b80fd5b5080fd5b8380fd5b8480fd5b8280fd5b634e487b7160e01b5f52604160045260245ffd5b90601f8019910116810190811067ffffffffffffffff82111761014357604052565b61010d565b604051906080820182811067ffffffffffffffff82111761014357604052565b67ffffffffffffffff811161014357601f01601f191660200190565b81601f820112156101ca5780359061019b82610168565b926101a96040519485610121565b828452602083830101116101ca57815f926020809301838601378301015290565b5f80fd5b5f5b8381106101df5750505f910152565b81810151838201526020016101d0565b6040916020825261020f81518092816020860152602086860191016101ce565b601f01601f1916010190565b9061022e602092828151948592016101ce565b0190565b61036661028e61032561035a9361030c6102fe8251926102da6102e06020830151926102da603b606060408401519301519560296040519c8d809c683d913730b6b2911d1160b91b6020830152602081519485930191016101ce565b8a0171111610113232b9b1b934b83a34b7b7111d1160711b60298201526102be82518093602086850191016101ce565b0101600d906c1116101134b6b0b3b2911d101160991b81520190565b9061021b565b71222c202261747472696275746573223a205b60701b815260120190565b615d7d60f01b815260020190565b0391610320601f1993848101835282610121565b61047b565b6040517f646174613a6170706c69636174696f6e2f6a736f6e3b6261736536342c0000006020820152938491603d83016102da565b03908101835282610121565b90565b604051906020820182811067ffffffffffffffff821117610143576040525f8252565b604051906060820182811067ffffffffffffffff82111761014357604052604082527f6768696a6b6c6d6e6f707172737475767778797a303132333435363738392b2f6040837f4142434445464748494a4b4c4d4e4f505152535455565758595a61626364656660208201520152565b634e487b7160e01b5f52601160045260245ffd5b906002820180921161041e57565b6103fc565b906020820180921161041e57565b600281901b91906001600160fe1b0381160361041e57565b9061045382610168565b6104606040519182610121565b8281528092610471601f1991610168565b0190602036910137565b8051156105645761048a61038c565b6104a66104a161049a8451610410565b6003900490565b610431565b916104b86104b384610423565b610449565b92835280815182019060208501935b828210610508575050506003905106806001146104f7576002146104e9575090565b603d60f81b5f199091015290565b50613d3d60f01b6001199091015290565b90919360049060038094019384516001603f81818460121c16880101519260f893841b8652828282600c1c1689010151841b8387015282828260061c1689010151841b60028701521686010151901b90820152019391906104c7565b5061036661036956fea264697066735822122068bab4620546ebb489f2599a5d5a7c8fc83603d8091ffe78066918ffac2c6dd764736f6c63430008140033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> NFTDescriptor:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[NFTDescriptor]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, NFTDescriptor, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[NFTDescriptor]]:
        return cls._deploy(request_type, [], return_tx, NFTDescriptor, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class TokenURIParams:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/NFTDescriptor.sol#10)

        Attributes:
            name (str): string
            description (str): string
            image (str): string
            attributes (str): string
        """
        original_name = 'TokenURIParams'

        name: str
        description: str
        image: str
        attributes: str


    @overload
    def constructTokenURI(self, params: NFTDescriptor.TokenURIParams, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/NFTDescriptor.sol#20)

        Args:
            params: struct NFTDescriptor.TokenURIParams
        Returns:
            string
        """
        ...

    @overload
    def constructTokenURI(self, params: NFTDescriptor.TokenURIParams, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/NFTDescriptor.sol#20)

        Args:
            params: struct NFTDescriptor.TokenURIParams
        Returns:
            string
        """
        ...

    @overload
    def constructTokenURI(self, params: NFTDescriptor.TokenURIParams, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/NFTDescriptor.sol#20)

        Args:
            params: struct NFTDescriptor.TokenURIParams
        Returns:
            string
        """
        ...

    @overload
    def constructTokenURI(self, params: NFTDescriptor.TokenURIParams, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/NFTDescriptor.sol#20)

        Args:
            params: struct NFTDescriptor.TokenURIParams
        Returns:
            string
        """
        ...

    def constructTokenURI(self, params: NFTDescriptor.TokenURIParams, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/kutu/projects/Vouch/new/vouch/contracts/Descriptors/NFTDescriptor.sol#20)

        Args:
            params: struct NFTDescriptor.TokenURIParams
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "92b4c81b", [params], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

NFTDescriptor.constructTokenURI.selector = b'\x92\xb4\xc8\x1b'
