# Setting Startup Options

We can create a startup script in the Python/IPython environment to import pandas and set options, which makes working with pandas more efficient.

```python
# This is an example of a startup script
# Place this in a .py file in the startup directory of IPython profile
import pandas as pd

pd.set_option("display.max_rows", 999)
pd.set_option("display.precision", 5)
```
