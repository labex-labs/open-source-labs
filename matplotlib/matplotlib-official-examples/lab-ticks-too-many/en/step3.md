# Handle Too Many Ticks

If the x-axis has many elements, all of which are strings, we may end up with too many ticks that are unreadable. In this case, we need to convert the strings to numeric types. Here is an example:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with 100 elements
x = [f'{xx}' for xx in np.arange(100)]
y = np.arange(100)

# plot the data with string tick labels
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('Categories')
plt.show()
```

In this example, we have 100 string values on the x-axis, resulting in too many ticks that are unreadable.

To fix this, we need to convert the strings to floats. Here is an example:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with 100 elements
x = [f'{xx}' for xx in np.arange(100)]
y = np.arange(100)

# convert strings to floats
x = np.asarray(x, float)

# plot the data with numeric tick labels
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('Floats')
plt.show()
```

In this example, we convert the string values to floats using `np.asarray()`. When we plot the data again, the tick labels are as expected.
