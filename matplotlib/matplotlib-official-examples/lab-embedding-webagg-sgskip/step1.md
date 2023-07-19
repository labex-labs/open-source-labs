# Create a Simple Example Figure

The first step is to create a simple example figure. In this case, we will create a figure that displays a sine wave.

```python
import numpy as np
import matplotlib.pyplot as plt

def create_figure():
    """
    Creates a simple example figure.
    """
    fig = plt.figure()
    ax = fig.add_subplot()
    t = np.arange(0.0, 3.0, 0.01)
    s = np.sin(2 * np.pi * t)
    ax.plot(t, s)
    return fig

figure = create_figure()
plt.show()
```
