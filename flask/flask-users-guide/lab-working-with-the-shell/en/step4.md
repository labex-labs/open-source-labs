# Improving the Shell Experience

To improve the shell experience, create a module (`shelltools.py`) with helper methods that can be imported into the interactive session. This module can contain additional helper methods for tasks such as initializing the database or dropping tables.

```python
# File: shelltools.py

def initialize_database():
    # Code to initialize the database
    pass

def drop_tables():
    # Code to drop tables
    pass
```

In the interactive shell, import the desired methods from the `shelltools` module.

```python
# File: shell.py
# Execution: python shell.py

from shelltools import initialize_database, drop_tables

# Import desired methods from shelltools module
from shelltools import *

# Use imported methods
initialize_database()
drop_tables()
```
