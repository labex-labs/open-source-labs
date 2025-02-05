# Create the Plot

Next, let's create a simple plot to work with. We will use NumPy to generate some random data to plot.

```python
import numpy as np

# Generate random data
np.random.seed(19680801)
data = 100 * np.random.rand(20)

# Create the plot
fig, ax = plt.subplots()
ax.plot(data)
```
