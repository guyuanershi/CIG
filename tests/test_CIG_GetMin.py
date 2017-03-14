from nose.tools import eq_
from nose.tools import with_setup
from src.CIG_GetMin import (push, pop, getMin, clear)


def setup_func():
    push(5)
    push(2)
    push(10)


def teardown_func():
    clear()


@with_setup(setup_func, teardown_func)
def test_minist():
    eq_(getMin(), 2)


@with_setup(setup_func, teardown_func)
def test_only_one_data():
    pop()
    pop()
    eq_(getMin(), 5)
