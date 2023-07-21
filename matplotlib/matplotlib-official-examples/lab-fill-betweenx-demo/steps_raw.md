# Matplotlib Fill Betweenx Tutorial

## Introduction

Matplotlib is a data visualization library in Python. It provides a wide variety of tools to create complex and customizable plots, charts, and graphs. One of the most useful tools provided by Matplotlib is the `fill_betweenx` function. This function is used to fill the area between two horizontal curves. In this tutorial, we will explore the `fill_betweenx` function and learn how to use it to create different types of plots.

## Steps

### Step 1: Plotting Simple Fill Betweenx

In this step, we will learn how to use the `fill_betweenx` function to create a simple plot. We will fill the area between two curves.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig, ax = plt.subplots(figsize=(6, 6))

ax.fill_betweenx(y, x1, x2, color='green', alpha=0.5)
ax.plot(x1, y, color='blue')
ax.plot(x2, y, color='red')

plt.show()
```

Output:
![Simple Fill Betweenx](https://i.imgur.com/9XKz7zD.png)

### Step 2: Creating Multiple Subplots

In this step, we will learn how to create multiple subplots and use the `fill_betweenx` function to fill the area between two horizontal curves in each subplot.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig, [ax1, ax2, ax3] = plt.subplots(1, 3, sharey=True, figsize=(12, 4))

ax1.fill_betweenx(y, 0, x1, color='green', alpha=0.5)
ax1.plot(x1, y, color='blue')
ax1.set_title('Fill between (x1, 0)')

ax2.fill_betweenx(y, x1, 1, color='red', alpha=0.5)
ax2.plot(x1, y, color='blue')
ax2.set_title('Fill between (x1, 1)')

ax3.fill_betweenx(y, x1, x2, color='orange', alpha=0.5)
ax3.plot(x1, y, color='blue')
ax3.plot(x2, y, color='red')
ax3.set_title('Fill between (x1, x2)')

plt.show()
```

Output:
![Multiple Subplots](https://i.imgur.com/UwJQKmJ.png)

### Step 3: Using Logical Conditions

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

### Step 4: Using Masked Arrays

In this step, we will learn how to use masked arrays to fill the area between two horizontal curves.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)
x2 = np.ma.masked_greater(x2, 1.0)

fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(x1, y, color='black')
ax.plot(x2, y, color='black')

ax.fill_betweenx(y, x1, x2, where=x2 >= x1, facecolor='green', alpha=0.5)
ax.fill_betweenx(y, x1, x2, where=x2 <= x1, facecolor='red', alpha=0.5)

plt.show()
```

Output:
![Using Masked Arrays](https://i.imgur.com/8D1r5Gf.png)

## Summary

In this tutorial, we learned how to use the `fill_betweenx` function in Matplotlib to fill the area between two horizontal curves. We also learned how to create multiple subplots and use logical conditions and masked arrays to create different types of plots. By using the `fill_betweenx` function, we can create complex and customizable plots in Python.
