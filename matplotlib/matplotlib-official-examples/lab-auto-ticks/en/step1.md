# Scatter plot without round_numbers autolimit_mode

In this step, we will create a scatter plot without round_numbers autolimit_mode and observe the behavior of tick auto-placement.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
ax.scatter(x, y, c=x+y)
plt.show()
```
