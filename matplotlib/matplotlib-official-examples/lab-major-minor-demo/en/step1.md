# Import the necessary libraries and create data

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
```

First, we import the necessary libraries, i.e., Matplotlib and NumPy. Then we create data to plot. In this example, we create a numpy array "t" and calculate another numpy array "s" using t.
