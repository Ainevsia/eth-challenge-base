#!/usr/bin/python3

import pytest


@pytest.fixture(scope="module")
def greeter_instance(Greeter, accounts):
    m = Greeter.deploy("HelloWorld", {'from': accounts[0]})
    yield m


def test_initial(greeter_instance):
    assert greeter_instance.greet() == "HelloWorld"


def test_solve(greeter_instance, accounts):
    greeter_instance.setGreeting("HelloChainFlag", {'from': accounts[0]})
    assert greeter_instance.isSolved() == True