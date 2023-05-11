import pytest

from settings import *

@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]

@pytest.fixture(scope="session")
def sender(accounts):
    return accounts[1]

@pytest.fixture(scope="session")
def recipient(accounts):
    return accounts[2]


@pytest.fixture(scope="module", autouse=True)
def vouch_nft(project, owner):

    vouch_nft = project.Vouch.deploy(sender=owner)
    return vouch_nft



