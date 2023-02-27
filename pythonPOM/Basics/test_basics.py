import os

import pytest

@pytest.mark.test1
def test_method1():
    print("test_method1")

@pytest.mark.test1
def test_method12():
    print("test_method12")

@pytest.mark.test2
def test_method123():
    print("test_method123")

@pytest.mark.test2
def test_method1234():
    print("test_method1234 | " + os.name)