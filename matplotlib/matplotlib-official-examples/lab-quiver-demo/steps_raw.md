# Advanced Quiver and Quiverkey Functions

## Introduction

Matplotlib is a data visualization library in Python that allows users to create a wide range of 2D and 3D plots. One of the many useful features of Matplotlib is the ability to create quiver plots, which display vector fields.

This lab will walk through some advanced options for the `quiver()` and `quiverkey()` functions in Matplotlib. These functions allow for customization of the arrows in a quiver plot, including arrow scale, pivot point, and arrow frequency.

## Steps

### Step 1: Arrows Scale with Plot Width, Not View

The `quiver()` function can be used to create a quiver plot. By default, the arrows in the plot will scale with the data, rather than the plot itself. This can make it difficult to see arrows that are close to the edge of the plot.

```python
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U = np.cos(X)
V = np.sin(Y)

fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
plt.show()
```

### Step 2: Pivot Point and Arrow Frequency

The `quiver()` function can also be used to customize the pivot point of the arrows and the frequency at which they are displayed. The `pivot` parameter can be set to `'mid'` or `'tip'`, and the arrays passed to `quiver()` can be sliced to display only every nth arrow.

```python
fig2, ax2 = plt.subplots()
ax2.set_title("pivot='mid'; every third arrow; units='inches'")
Q = ax2.quiver(X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3],
               pivot='mid', units='inches')
qk = ax2.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
ax2.scatter(X[::3, ::3], Y[::3, ::3], color='r', s=5)
plt.show()
```

### Step 3: Scale Arrows with X View

The `quiver()` function also allows for scaling arrows with the x view. This can be useful for displaying arrows at different scales depending on the data.

```python
fig3, ax3 = plt.subplots()
ax3.set_title("pivot='tip'; scales with x view")
M = np.hypot(U, V)
Q = ax3.quiver(X, Y, U, V, M, units='x', pivot='tip', width=0.022,
               scale=1 / 0.15)
qk = ax3.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
ax3.scatter(X, Y, color='0.5', s=1)
plt.show()
```

## Summary

This lab covered some advanced options for the `quiver()` and `quiverkey()` functions in Matplotlib. These options allow for customization of the arrows in a quiver plot, including arrow scale, pivot point, and arrow frequency. By using these options, users can create more informative and visually appealing quiver plots.
