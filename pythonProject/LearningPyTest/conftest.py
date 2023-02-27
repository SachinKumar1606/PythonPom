import pytest


@pytest.yield_fixture(scope='function', autouse=True)
def testToLaunch():
    print("test to launch")
    print("login")
    yield
    print("logout")
    print("close Browser")
