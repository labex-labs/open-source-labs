# Setup and Create Sample Data

Before we start, let's import necessary modules and create a sample DataFrame.

```python
# Import necessary modules
import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame(
    {
        "a": np.random.randn(1000),
        "b": np.random.randn(1000),
        "N": np.random.randint(100, 1000, (1000)),
        "x": "x",
    }
)
df
```
