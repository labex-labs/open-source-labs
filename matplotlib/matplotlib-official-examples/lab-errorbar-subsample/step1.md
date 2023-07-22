# Import Libraries and Generate Data

First, we need to import the necessary libraries and generate some example data to work with. In this example, we will use numpy to generate the data and matplotlib to visualize it.

```python
import matplotlib.pyplot as plt
import numpy as np

# example data
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# example variable error bar values
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)
```
