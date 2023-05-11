import pytest

import ape
from settings import *


def test_init_vouch_nft(vouch_nft, sender, recipient):
    success = vouch_nft.vouch(recipient, "Test", sender=sender)
    assert success

