from datetime import datetime, timedelta

def add_days(n, d = datetime.today()):
  return d + timedelta(n)

please generate the python test code for the above function. must be in the format of:

```py
import unittest
from solution import 

class ClassName(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
```

please make sure the test code is runnable and the function is correct.