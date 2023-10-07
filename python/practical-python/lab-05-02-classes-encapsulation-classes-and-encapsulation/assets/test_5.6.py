import sys


sys.path.append("/home/labex/project")
from stock import Stock

s = Stock("GOOG", 100, 490.1)
assert s.cost == 49010.0

try:
    s.cost()
except TypeError as e:
    assert str(e) == "'float' object is not callable"
else:
    raise AssertionError("TypeError not raised")
