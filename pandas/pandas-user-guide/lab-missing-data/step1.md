# Import Necessary Libraries and Create DataFrame

To start, we need to import the necessary libraries - pandas and NumPy. Then, we'll create a DataFrame with some missing values.

```python
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame(
   np.random.randn(5, 3),
   index=["a", "c", "e", "f", "h"],
   columns=["one", "two", "three"],
)
df["four"] = "bar"
df["five"] = df["one"] > 0
df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
```
