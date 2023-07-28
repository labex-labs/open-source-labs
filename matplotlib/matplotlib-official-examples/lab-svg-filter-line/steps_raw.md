# Matplotlib SVG Filter Line Lab

## Introduction

This lab demonstrates how to use SVG filtering effects with Matplotlib. The filtering effects are only effective if your SVG renderer supports it.

## Steps

### Step 1: Import Required Libraries

First, we need to import the required libraries: `matplotlib.pyplot`, `io` and `xml.etree.ElementTree`.

```python
import io
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
```

### Step 2: Create a Figure and Axes

We create a figure object with `plt.figure()` and add an axes object using `fig1.add_axes()`. We also set the size and position of the axes using `[0.1, 0.1, 0.8, 0.8]`.

```python
fig1 = plt.figure()
ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
```

### Step 3: Draw Lines

We draw two lines using `ax.plot()`. We also customize the lines with different colors, markers, and labels.

```python
l1, = ax.plot([0.1, 0.5, 0.9], [0.1, 0.9, 0.5], "bo-", mec="b", lw=5, ms=10, label="Line 1")
l2, = ax.plot([0.1, 0.5, 0.9], [0.5, 0.2, 0.7], "rs-", mec="r", lw=5, ms=10, label="Line 2")
```

### Step 4: Draw Shadows

We draw shadows for the lines by using the same lines with a slight offset and gray colors. We adjust the color and zorder of the shadow lines so that they are drawn below the original lines. We also use the `offset_copy()` method to create an offset transform for the shadow lines.

```python
for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()
    shadow, = ax.plot(xx, yy)
    shadow.update_from(l)

    shadow.set_color("0.2")
    shadow.set_zorder(l.get_zorder() - 0.5)

    transform = mtransforms.offset_copy(l.get_transform(), fig1, x=4.0, y=-6.0, units='points')
    shadow.set_transform(transform)

    shadow.set_gid(l.get_label() + "_shadow")
```

### Step 5: Set Axes Limits and Save Figure

We set the x and y limits for the axes and save the figure as a bytes string in the SVG format using `io.BytesIO()` and `plt.savefig()`.

```python
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)

f = io.BytesIO()
plt.savefig(f, format="svg")
```

### Step 6: Define Filter

We define a filter for a Gaussian blur using the `<defs>` and `<filter>` tags with the `stdDeviation` attribute.

```python
filter_def = """
  <defs xmlns='http://www.w3.org/2000/svg'
        xmlns:xlink='http://www.w3.org/1999/xlink'>
    <filter id='dropshadow' height='1.2' width='1.2'>
      <feGaussianBlur result='blur' stdDeviation='3'/>
    </filter>
  </defs>
"""
```

### Step 7: Read and Modify SVG

We read in the saved SVG using `ET.XMLID()` and insert the filter definition in the SVG DOM tree using `tree.insert()`. We then pick up the SVG element with the given ID and apply the shadow filter using `shadow.set()`.

```python
tree, xmlid = ET.XMLID(f.getvalue())

tree.insert(0, ET.XML(filter_def))

for l in [l1, l2]:
    shadow = xmlid[l.get_label() + "_shadow"]
    shadow.set("filter", 'url(#dropshadow)')

fn = "svg_filter_line.svg"
print(f"Saving '{fn}'")
ET.ElementTree(tree).write(fn)
```

## Summary

This lab demonstrated how to use SVG filtering effects with Matplotlib. We learned how to create a figure and axes, draw lines and shadows, set axes limits, and define and apply filters to an SVG.
