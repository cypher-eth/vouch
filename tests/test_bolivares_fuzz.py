import random
import string
from woke.testing import *
from woke.testing.fuzzing import *
from woke.development.transactions import *

from pytypes.contracts.Bolivares import Bolivares

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

class CounterTest(FuzzTest):
    _bolivares: Bolivares
    _owner: Account

    # executed before each sequence
    def pre_sequence(self) -> None:
        self._owner = random_account()
        self._bolivares = Bolivares.deploy(from_=self._owner)

    @flow()
    def flow_register(self):
        barcode = ''.join(random.choices(string.ascii_lowercase, k=32))
        user = random_account()
        self.register(user, barcode)
        with may_revert(Error('Cannot register same bill twice')) as e:
            self._bolivares.register(barcode, from_=user)


    @flow()
    def flow_unregister(self):
        barcode = ''.join(random.choices(string.ascii_lowercase, k=32))
        user = random_account()
        
        # FAILING UNREGISTER
        with may_revert(Error('Barcode is not registered')) as e:
            self._bolivares.unregister(barcode, from_=user)

        # REGISTER
        self.register(user, barcode)

        # UNREGISTER
        self._bolivares.unregister(barcode, from_=user)
        assert self._bolivares.getUserFromVouch(barcode) == ZERO_ADDRESS
        assert self._bolivares.userBarcode(user.address) == ""

    # execute this flow less often (the default weight is 100)
    @flow(weight=60)
    def flow_vouch(self):
        barcode = ''.join(random.choices(string.ascii_lowercase, k=32))
        user = default_chain.accounts[0]
        voucher = default_chain.accounts[1]
        
        self.register(user, barcode)
        message = 'Vouch message'
        self._bolivares.vouch(barcode, message, from_=voucher)


    def register(self, account, barcode):
        self._bolivares.register(barcode, from_=account)
        assert self._bolivares.getUserFromVouch(barcode) == account.address
        assert self._bolivares.userBarcode(account.address) == barcode


@default_chain.connect()
def test_counter_fuzz():
    # run 10 independent test sequences (the chain is reset between each sequence) with 100 flows in each
    CounterTest().run(sequences_count=10, flows_count=100)