
import woke.development.core
from woke.utils import get_package_version

if get_package_version("woke") != "3.4.2":
    raise RuntimeError("Pytypes generated for a different version of woke. Please regenerate.")

woke.development.core.errors = {b'\x08\xc3y\xa0': {'': ('woke.development.transactions', ('Error',))}, b'NH{q': {'': ('woke.development.transactions', ('Panic',))}}
woke.development.core.events = {b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%': {'contracts/Tokens/ERC721.sol:ERC721': ('pytypes.contracts.Tokens.ERC721', ('ERC721', 'Approval'))}, b'\x170~\xab9\xaba\x07\xe8\x89\x98E\xad=Y\xbd\x96S\xf2\x00\xf2 \x92\x04\x89\xca+Y7il1': {'contracts/Tokens/ERC721.sol:ERC721': ('pytypes.contracts.Tokens.ERC721', ('ERC721', 'ApprovalForAll'))}, b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef': {'contracts/Tokens/ERC721.sol:ERC721': ('pytypes.contracts.Tokens.ERC721', ('ERC721', 'Transfer')), 'contracts/Tokens/ERC721S.sol:ERC721S': ('pytypes.contracts.Tokens.ERC721S', ('ERC721S', 'Transfer')), 'contracts/Bolivares.sol:Bolivares': ('pytypes.contracts.Tokens.ERC721S', ('ERC721S', 'Transfer')), 'contracts/VouchNFT.sol:VouchNFT': ('pytypes.contracts.Tokens.ERC721S', ('ERC721S', 'Transfer'))}, b'KS8T\x0bM\x1c\x0fm\xd00\x8a%\xf63\xb7\xff`G/\x89Mq\x1c\xff\x9d\xd6N5\xc6\x13\xb2': {'contracts/Utils/Documents.sol:Documents': ('pytypes.contracts.Utils.Documents', ('Documents', 'DocumentRemoved')), 'contracts/Bolivares.sol:Bolivares': ('pytypes.contracts.Utils.Documents', ('Documents', 'DocumentRemoved'))}, b'\xba\xa2\x06\xe5\xea\x80\x0e\xb8\x8b\xce\t\x9fE?\xeeS)[y;\x9d]\x1c\xfcL\xe4\xb6\xdb\x06\xa3OS': {'contracts/Utils/Documents.sol:Documents': ('pytypes.contracts.Utils.Documents', ('Documents', 'DocumentUpdated')), 'contracts/Bolivares.sol:Bolivares': ('pytypes.contracts.Utils.Documents', ('Documents', 'DocumentUpdated'))}}
woke.development.core.contracts_by_fqn = {'contracts/Interfaces/IMasterContract.sol:IMasterContract': ('pytypes.contracts.Interfaces.IMasterContract', ('IMasterContract',)), 'contracts/Interfaces/IContract.sol:IContract': ('pytypes.contracts.Interfaces.IContract', ('IContract',)), 'contracts/Interfaces/ITokenURIFetcher.sol:ITokenURIFetcher': ('pytypes.contracts.Interfaces.ITokenURIFetcher', ('ITokenURIFetcher',)), 'contracts/Tokens/ERC721.sol:ERC721': ('pytypes.contracts.Tokens.ERC721', ('ERC721',)), 'contracts/Tokens/ERC721.sol:ERC721TokenReceiver': ('pytypes.contracts.Tokens.ERC721', ('ERC721TokenReceiver',)), 'contracts/Tokens/ERC721S.sol:ERC721S': ('pytypes.contracts.Tokens.ERC721S', ('ERC721S',)), 'contracts/Tokens/ERC721S.sol:ERC721TokenReceiver': ('pytypes.contracts.Tokens.ERC721S', ('ERC721TokenReceiver',)), 'contracts/Utils/Base64.sol:Base64': ('pytypes.contracts.Utils.Base64', ('Base64',)), 'contracts/Descriptors/NFTDescriptor.sol:NFTDescriptor': ('pytypes.contracts.Descriptors.NFTDescriptor', ('NFTDescriptor',)), 'contracts/Utils/BokkyPooBahsDateTimeLibrary.sol:BokkyPooBahsDateTimeLibrary': ('pytypes.contracts.Utils.BokkyPooBahsDateTimeLibrary', ('BokkyPooBahsDateTimeLibrary',)), 'contracts/Descriptors/BolivaresDescriptor.sol:BolivaresDescriptor': ('pytypes.contracts.Descriptors.BolivaresDescriptor', ('BolivaresDescriptor',)), 'contracts/Descriptors/VouchDescriptor.sol:VouchDescriptor': ('pytypes.contracts.Descriptors.VouchDescriptor', ('VouchDescriptor',)), 'contracts/Utils/Documents.sol:Documents': ('pytypes.contracts.Utils.Documents', ('Documents',)), 'contracts/Bolivares.sol:Bolivares': ('pytypes.contracts.Bolivares', ('Bolivares',)), 'contracts/Vouch.sol:Vouch': ('pytypes.contracts.Vouch', ('Vouch',)), 'contracts/VouchNFT.sol:Vouch': ('pytypes.contracts.VouchNFT', ('Vouch',)), 'contracts/VouchNFT.sol:VouchNFT': ('pytypes.contracts.VouchNFT', ('VouchNFT',))}
woke.development.core.contracts_by_metadata = {b'\xa2dipfsX"\x12 \xf3\x9ci\xbe\x07V\xbff\'e\xb0ZM\x18A;\x9a\x14\n\xc1\x18\xac\xd5!\xf4\xd47rR\xc7a\x95dsolcC\x00\x08\x14\x003': 'contracts/Utils/Base64.sol:Base64', b'\xa2dipfsX"\x12 h\xba\xb4b\x05F\xeb\xb4\x89\xf2Y\x9a]Z|\x8f\xc86\x03\xd8\t\x1f\xfex\x06i\x18\xff\xac,m\xd7dsolcC\x00\x08\x14\x003': 'contracts/Descriptors/NFTDescriptor.sol:NFTDescriptor', b'\xa2dipfsX"\x12 \x13\xbb\xd5\xb6\x95o4yh\xee\x0b\xb0\xad\x02\xdc\x8a\xac[lZ t#\xaf\xec\x89L1\x87\r\xe2\xe5dsolcC\x00\x08\x14\x003': 'contracts/Utils/BokkyPooBahsDateTimeLibrary.sol:BokkyPooBahsDateTimeLibrary', b'\xa2dipfsX"\x12 \xb8\xeeW\xcbs7\x81i\x8e\xd9\x94\x11\xa6\x82:\x0c\xfe \xa0\xbd\xd7v\xa4D.0\x987.\xe07\xd5dsolcC\x00\x08\x14\x003': 'contracts/Utils/Documents.sol:Documents', b'\xa2dipfsX"\x12 S\xf3\x02#\x0creY\xe1;W\x00\xda=,L\xe7\x97\xbc$\x9d\xc6\x8an\x1e)\xef\x93\xea\xa8\x1c]dsolcC\x00\x08\x14\x003': 'contracts/Bolivares.sol:Bolivares', b'\xa2dipfsX"\x12 \xd7P\x9f\x07\x8c\x1e*\x88\xd6\xae\xf3\x8c\xd9\xf6\xde\tN9q\x8d\x1e\xd7\r\n\xc1i]\xc9\xb6\xb0\xa7%dsolcC\x00\x08\x14\x003': 'contracts/Vouch.sol:Vouch', b'\xa2dipfsX"\x12 1\x1f#\x9a\xfe,\x90N\xd9\x89\x99\xa6\x0b\x8b\x95\xac\xa6X\xb1\x1f\x0e\xe4\x04\x12\xeb*\xf6\x03\x8d\x0c\x81\xbddsolcC\x00\x08\x14\x003': 'contracts/VouchNFT.sol:VouchNFT'}
woke.development.core.contracts_inheritance = {'contracts/Interfaces/IMasterContract.sol:IMasterContract': ('contracts/Interfaces/IMasterContract.sol:IMasterContract',), 'contracts/Interfaces/IContract.sol:IContract': ('contracts/Interfaces/IContract.sol:IContract', 'contracts/Interfaces/IMasterContract.sol:IMasterContract'), 'contracts/Interfaces/ITokenURIFetcher.sol:ITokenURIFetcher': ('contracts/Interfaces/ITokenURIFetcher.sol:ITokenURIFetcher',), 'contracts/Tokens/ERC721.sol:ERC721': ('contracts/Tokens/ERC721.sol:ERC721',), 'contracts/Tokens/ERC721.sol:ERC721TokenReceiver': ('contracts/Tokens/ERC721.sol:ERC721TokenReceiver',), 'contracts/Tokens/ERC721S.sol:ERC721S': ('contracts/Tokens/ERC721S.sol:ERC721S',), 'contracts/Tokens/ERC721S.sol:ERC721TokenReceiver': ('contracts/Tokens/ERC721S.sol:ERC721TokenReceiver',), 'contracts/Utils/Base64.sol:Base64': ('contracts/Utils/Base64.sol:Base64',), 'contracts/Descriptors/NFTDescriptor.sol:NFTDescriptor': ('contracts/Descriptors/NFTDescriptor.sol:NFTDescriptor',), 'contracts/Utils/BokkyPooBahsDateTimeLibrary.sol:BokkyPooBahsDateTimeLibrary': ('contracts/Utils/BokkyPooBahsDateTimeLibrary.sol:BokkyPooBahsDateTimeLibrary',), 'contracts/Descriptors/BolivaresDescriptor.sol:BolivaresDescriptor': ('contracts/Descriptors/BolivaresDescriptor.sol:BolivaresDescriptor', 'contracts/Descriptors/NFTDescriptor.sol:NFTDescriptor'), 'contracts/Descriptors/VouchDescriptor.sol:VouchDescriptor': ('contracts/Descriptors/VouchDescriptor.sol:VouchDescriptor', 'contracts/Descriptors/NFTDescriptor.sol:NFTDescriptor'), 'contracts/Utils/Documents.sol:Documents': ('contracts/Utils/Documents.sol:Documents',), 'contracts/Bolivares.sol:Bolivares': ('contracts/Bolivares.sol:Bolivares', 'contracts/Descriptors/BolivaresDescriptor.sol:BolivaresDescriptor', 'contracts/Descriptors/NFTDescriptor.sol:NFTDescriptor', 'contracts/Tokens/ERC721S.sol:ERC721S', 'contracts/Utils/Documents.sol:Documents'), 'contracts/Vouch.sol:Vouch': ('contracts/Vouch.sol:Vouch',), 'contracts/VouchNFT.sol:Vouch': ('contracts/VouchNFT.sol:Vouch',), 'contracts/VouchNFT.sol:VouchNFT': ('contracts/VouchNFT.sol:VouchNFT', 'contracts/Descriptors/VouchDescriptor.sol:VouchDescriptor', 'contracts/Descriptors/NFTDescriptor.sol:NFTDescriptor', 'contracts/Tokens/ERC721S.sol:ERC721S')}
woke.development.core.contracts_revert_index = {}
woke.development.core.creation_code_index = [(((85, b'\x83\xd6(yfG\xad\xc7\xbc+\xf0\xfa(\x8b\x18QI\x97\xc7k\xb3\xe9m\xcf\x8c\xb3\xbc\x84\xde\xae\xd8\xd0'),), 'contracts/Utils/Base64.sol:Base64'), (((1470, b'\xffX\xb4Q8z`^\x01\xef\xdc\xed\xb3M\xf8\xfd\x90>\xa6\nvH\xe2\x89\xb0\x85\xac\xf8\x0c\x9c\x11\xf0'),), 'contracts/Descriptors/NFTDescriptor.sol:NFTDescriptor'), (((85, b'\x7f\xd2E\xeb\x81-\x7f\xb9@\xbd=,(b\xbc\xceV$QSg\x88\x95\xd5\x83!l\x84x$\x1am'),), 'contracts/Utils/BokkyPooBahsDateTimeLibrary.sol:BokkyPooBahsDateTimeLibrary'), (((1048, b'\xc3\xfeI\xa1*\x9b?\xba\x07\x17?`\x16(a\xce\xc5\xfai\xba^W8Ir\xc9\xee\x1d\x83\xd6\xa0\x81'),), 'contracts/Utils/Documents.sol:Documents'), (((16290, b'3#\xe5\x08\x06 P\x13\xca\xf4\xb9\xf9\x97=B\x08\xe1\x10\x1e\x00\xf7\x17\xe8 \x85\xac\xc3\xb5\x95Y\xef\xa3'),), 'contracts/Bolivares.sol:Bolivares'), (((1863, b'\xf4\x07\xc8F\xb6 \xb0md\x01\xeer\x10\xf7\xbd\x1aia\x85#_\xa9\t\xac\xe2L>\xc4\xa3\x1f<\xa8'),), 'contracts/Vouch.sol:Vouch'), (((10112, b'\x9a\x99\xd9*\x19\xd6\xb4\xb8F$\x17\x1f\x12\xec?\xc8ix*\xfd\x1cV_\x0c\xbd\x9eS6\xb6*\xdd$'),), 'contracts/VouchNFT.sol:VouchNFT')]
