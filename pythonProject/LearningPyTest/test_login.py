import pytest


@pytest.mark.smoke
def testLogin():
    print('test login')


@pytest.mark.sanity
def testAssertion():
    assert 2 + 3 == 5
