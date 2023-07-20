# Creating a Structured Array

To create a structured array, we can use the `np.array` function and specify the data type using the `dtype` parameter. The data type should be a list of tuples, where each tuple represents a field in the structured array. Each tuple should contain the field name and the data type of the field.

```python
import numpy as np

# Create a structured array
x = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
