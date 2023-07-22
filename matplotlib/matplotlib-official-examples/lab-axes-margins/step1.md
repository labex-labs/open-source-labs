# Plotting with Margins

The `margins()` method in Matplotlib can be used to set margins in the plot instead of using `set_xlim()` and `set_ylim()` methods. In this step, we will learn how to zoom in and out of a plot using `margins()` method instead of `set_xlim()` and `set_ylim()` methods.

```python
import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 3.0, 0.01)

# create a subplot with margins
ax1 = plt.subplot(212)
ax1.margins(0.05) # default margin is 0.05, value 0 means fit
ax1.plot(t1, f(t1))

# create a subplot with zoomed out margins
ax2 = plt.subplot(221)
ax2.margins(2, 2) # values >0.0 zoom out
ax2.plot(t1, f(t1))
ax2.set_title('Zoomed out')

# create a subplot with zoomed in margins
ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25) # values in (-0.5, 0.0) zooms in to center
ax3.plot(t1, f(t1))
ax3.set_title('Zoomed in')

plt.show()
```
