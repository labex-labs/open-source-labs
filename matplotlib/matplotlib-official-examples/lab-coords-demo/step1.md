# Creating a Sine Wave Plot

First, we need to create a sine wave plot using numpy and matplotlib libraries.

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
```
