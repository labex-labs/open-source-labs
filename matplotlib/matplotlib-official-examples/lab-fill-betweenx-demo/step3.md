# Using Logical Conditions

In this step, we will learn how to use logical conditions to fill the area between two horizontal curves.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(x1, y, color='black')
ax.plot(x2, y, color='black')

ax.fill_betweenx(y, x1, x2, where=x2 >= x1, facecolor='green', alpha=0.5)
ax.fill_betweenx(y, x1, x2, where=x2 <= x1, facecolor='red', alpha=0.5)

plt.show()
```

Output:
![Using Logical Conditions](https://i.imgur.com/1JnRf0k.png)
