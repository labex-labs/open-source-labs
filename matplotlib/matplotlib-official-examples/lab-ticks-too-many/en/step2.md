# Convert Strings to Numeric Types

To fix the tick behavior, we need to convert the strings to numeric types. Here is an example:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# convert strings to floats
x = np.asarray(x, dtype='float')

# plot the data with numeric tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Floats')
plt.show()
```

In this example, we convert the string values to floats using `np.asarray()`. When we plot the data again, the tick labels are as expected.
