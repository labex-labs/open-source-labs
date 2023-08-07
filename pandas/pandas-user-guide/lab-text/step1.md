# Store Text Data

In pandas, you can store text data in two ways: using an `object` dtype NumPy array or a `StringDtype` extension type. We recommend using `StringDtype` because it's safer and more specific than the generic `object` dtype.

```python
import pandas as pd

# create a series with `object` dtype
s1 = pd.Series(["a", "b", "c"], dtype="object")

# create a series with `StringDtype`
s2 = pd.Series(["a", "b", "c"], dtype="string")
```
