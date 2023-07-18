# Create a Matplotlib Figure

Next, we will create a Matplotlib figure using the `Figure` class. We will also add a subplot to the figure, plot a sine wave using NumPy, and label the axes.

```python
import numpy as np
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot()
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2*np.pi*t)
ax.plot(t, s)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Sine Wave')
```
