# Create a damped and undamped oscillation plot

First, we will create a figure with two subplots, one for a damped oscillation and another for an undamped oscillation. We will use the `np.linspace()` function to create an array of time values and then plot the corresponding amplitude values for each type of oscillation using the `np.cos()` and `np.exp()` functions.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('damped')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('amplitude')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('time (s)')
ax2.set_title('undamped')

fig.suptitle('Different types of oscillations', fontsize=16)

plt.show()
```
