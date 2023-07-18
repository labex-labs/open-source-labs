# Matplotlib AsinhScale Lab

## Introduction

Matplotlib is a powerful data visualization library in Python. It provides a variety of tools for creating a wide range of graphs, charts, and plots. One of the most powerful features of Matplotlib is its ability to scale data. This lab will introduce you to the AsinhScale, which is a transformation that allows for plotting quantities that cover a very wide dynamic range that includes both positive and negative values.

## Steps

### Step 1: Install Matplotlib

Before starting, make sure that Matplotlib is installed. You can install it using pip command as follows:

```python
pip install matplotlib
```

### Step 2: Import Required Libraries

To use the AsinhScale, we need to import the Matplotlib library and the numpy library. Numpy is a powerful numerical computing library in Python that is often used in conjunction with Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 3: Create Sample Data

Before we can plot data using the AsinhScale, we need to create some sample data. We will create a simple line graph using numpy's linspace method.

```python
# Prepare sample values for variations on y=x graph:
x = np.linspace(-3, 6, 500)
```

### Step 4: Compare "symlog" and "asinh" behaviour on sample y=x graph

We will compare the behaviour of "symlog" and "asinh" on a sample y=x graph. We will plot the same graph twice, once with "symlog" and once with "asinh".

```python
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex=True)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')
```

### Step 5: Compare "asinh" graphs with different scale parameter "linear_width"

We will now compare "asinh" graphs with different scale parameters "linear_width". We will plot three graphs with different "linear_width" values.

```python
fig2 = plt.figure(layout='constrained')
axs = fig2.subplots(1, 3, sharex=True)
for ax, (a0, base) in zip(axs, ((0.2, 2), (1.0, 0), (5.0, 10))):
    ax.set_title(f'linear_width={a0:.3g}')
    ax.plot(x, x, label='y=x')
    ax.plot(x, 10*x, label='y=10x')
    ax.plot(x, 100*x, label='y=100x')
    ax.set_yscale('asinh', linear_width=a0, base=base)
    ax.grid()
    ax.legend(loc='best', fontsize='small')
```

### Step 6: Compare "symlog" and "asinh" scalings on 2D Cauchy-distributed random numbers

Finally, we will compare "symlog" and "asinh" scalings on 2D Cauchy-distributed random numbers. We will plot the same graph twice, once with "symlog" and once with "asinh".

```python
fig3 = plt.figure()
ax = fig3.subplots(1, 1)
r = 3 * np.tan(np.random.uniform(-np.pi / 2.02, np.pi / 2.02,
                                 size=(5000,)))
th = np.random.uniform(0, 2*np.pi, size=r.shape)

ax.scatter(r * np.cos(th), r * np.sin(th), s=4, alpha=0.5)
ax.set_xscale('asinh')
ax.set_yscale('symlog')
ax.set_xlabel('asinh')
ax.set_ylabel('symlog')
ax.set_title('2D Cauchy random deviates')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.grid()
```

## Summary

This lab introduced the AsinhScale in Matplotlib, which is a transformation that allows for plotting quantities that cover a very wide dynamic range that includes both positive and negative values. We learned how to create sample data and how to plot graphs with "symlog" and "asinh". We also learned how to compare "asinh" graphs with different scale parameters and how to compare "symlog" and "asinh" scalings on 2D Cauchy-distributed random numbers.
