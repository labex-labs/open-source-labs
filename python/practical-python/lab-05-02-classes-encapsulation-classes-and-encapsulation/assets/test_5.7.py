import sys


sys.path.append('/home/labex/project')

from stock import Stock

s = Stock('GOOG', 100, 490.10)

s.shares = 50
assert s.shares == 50

try:
    s.shares = 'a lot'
except TypeError as e:
    assert str(e) == "Expected an integer"
else:
    raise AssertionError("TypeError not raised")