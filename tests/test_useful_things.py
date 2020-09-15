import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import useful_things
from hypothesis import given
import hypothesis.strategies as st


@given(st.integers(), st.integers())
def test_add(x, y):
    assert useful_things.add(x, y) == x + y


@given(st.integers(), st.integers())
def test_subtract(x, y):
    assert useful_things.subtract(x, y) == x - y
