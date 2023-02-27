import pytest


@pytest.fixture(params=["a", "b"])
def demo_fix(request):
    print(request.param)


def testToAdd(demo_fix):
    print("test to add")


@pytest.mark.parametrize("a, b, final", [(5, 5, 10), (6, 10, 16)])
def testAddition(a, b, final):
    assert a + b == final

# def testToRemove(demo_fix):
#     print("test to remove")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption(--browser)


def testToRemove(browser):
    print("test to remove")
