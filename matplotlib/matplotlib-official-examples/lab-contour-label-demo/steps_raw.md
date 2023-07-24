# Matplotlib Contour Label Tutorial

## Introduction

In this tutorial, we will learn how to create contour labels in Matplotlib. Contour labels are used to label the contours in a contour plot. This tutorial will cover some advanced techniques for creating custom contour labels.

## Steps

### Step 1: Define our surface

We will start by defining our surface using numpy and matplotlib. This will give us a dataset to work with.

```python
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```

### Step 2: Make contour labels with custom level formatters

We will now create contour labels with custom level formatters. This will allow us to format the labels in a specific way. In this case, we will remove trailing zeros and add a percent sign.

```python
def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s} \%" if plt.rcParams["text.usetex"] else f"{s} %"

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)
```

### Step 3: Label contours with arbitrary strings using a dictionary

We can also label contours with arbitrary strings using a dictionary. This will allow us to label the contours with custom labels. In this example, we will use a list of strings to label the contours.

```python
fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s

ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
```

### Step 4: Use a Formatter

We can also use a formatter to format the contour labels. This will allow us to format the labels in a specific way. In this example, we will use a LogFormatterMathtext to format the labels.

```python
fig2, ax2 = plt.subplots()
CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
fmt = ticker.LogFormatterMathtext()
fmt.create_dummy_axis()
ax2.clabel(CS2, CS2.levels, fmt=fmt)
ax2.set_title("$100^Z$")

plt.show()
```

## Summary

In this tutorial, we learned how to create contour labels in Matplotlib. We covered some advanced techniques for creating custom contour labels, including custom level formatters, labeling contours with arbitrary strings, and using a formatter to format the contour labels. These techniques can be useful for creating visualizations that are both informative and aesthetically pleasing.
