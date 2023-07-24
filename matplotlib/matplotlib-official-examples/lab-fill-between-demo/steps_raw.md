# Matplotlib Fill Between Lab

## Introduction

Matplotlib is a data visualization library in Python programming language. It is used to create static, animated, and interactive visualizations in Python. In this lab, you will learn how to use `fill_between` function from Matplotlib to fill the area between two lines.

## Steps

### Step 1: Basic Usage

The `fill_between` function can be used to fill the area between two lines. The parameters _y1_ and _y2_ can be scalars, indicating a horizontal boundary at the given y-values. If only _y1_ is given, _y2_ defaults to 0.

```python
x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 0.8 * np.sin(4 * np.pi * x)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(6, 6))

ax1.fill_between(x, y1)
ax1.set_title('fill between y1 and 0')

ax2.fill_between(x, y1, 1)
ax2.set_title('fill between y1 and 1')

ax3.fill_between(x, y1, y2)
ax3.set_title('fill between y1 and y2')
ax3.set_xlabel('x')
fig.tight_layout()
```

### Step 2: Confidence Bands

A common application for `fill_between` is the indication of confidence bands. `fill_between` uses the colors of the color cycle as the fill color. It is therefore often a good practice to lighten the color by making the area semi-transparent using _alpha_.

```python
N = 21
x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# fit a linear curve and estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')
```

### Step 3: Selectively Filling Horizontal Regions

The parameter _where_ allows to specify the x-ranges to fill. It's a boolean array with the same size as _x_. Only x-ranges of contiguous _True_ sequences are filled. As a result, the range between neighboring _True_ and _False_ values is never filled. It is therefore recommended to set `interpolate=True` unless the x-distance of the data points is fine enough so that the above effect is not noticeable.

```python
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title('interpolation=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolation=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                 interpolate=True)
ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                 interpolate=True)
fig.tight_layout()
```

### Step 4: Selectively Marking Horizontal Regions Across the Whole Axes

The same selection mechanism can be applied to fill the full vertical height of the axes. To be independent of y-limits, we add a transform that interprets the x-values in data coordinates and the y-values in axes coordinates. The following example marks the regions in which the y-data are above a given threshold.

```python
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color='black')

threshold = 0.75
ax.axhline(threshold, color='green', lw=2, alpha=0.7)
ax.fill_between(x, 0, 1, where=y > threshold,
                color='green', alpha=0.5, transform=ax.get_xaxis_transform())
```

## Summary

In this lab, you learned how to use `fill_between` function from Matplotlib to fill the area between two lines. You also learned how to selectively fill horizontal regions and mark horizontal regions across the whole axes.
