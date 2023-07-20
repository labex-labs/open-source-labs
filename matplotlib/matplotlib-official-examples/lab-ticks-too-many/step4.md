# Handle DateTime Ticks

When working with datetime values on the x-axis, it is important to convert the strings to datetime objects to get the proper date locators and formatters. Here is an example:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with datetime strings
x = ['2021-10-01', '2021-11-02', '2021-12-03', '2021-09-01']
y = [0, 2, 3, 1]

# convert strings to datetime64
x = np.asarray(x, dtype='datetime64[s]')

# plot the data with datetime tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.tick_params(axis='x', labelrotation=90)
plt.show()
```

In this example, we convert the string values to datetime64 using `np.asarray()`. When we plot the data again, the tick labels are as expected.
