# Constructing Nullable Integer Arrays

Pandas provides the `IntegerArray` class for creating arrays of nullable integers. Let's start by creating an `IntegerArray`.

```python
# Import necessary libraries
import pandas as pd
import numpy as np

# Create an IntegerArray with missing values
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
# Output: <IntegerArray>
# [1, 2, <NA>]
# Length: 3, dtype: Int64
```

You can also use the string alias "Int64" to specify the data type when creating the array. All NA-like values are replaced with `pandas.NA`.

```python
# Create an IntegerArray using the "Int64" string alias
arr = pd.array([1, 2, np.nan], dtype="Int64")
# Output: <IntegerArray>
# [1, 2, <NA>]
# Length: 3, dtype: Int64
```
