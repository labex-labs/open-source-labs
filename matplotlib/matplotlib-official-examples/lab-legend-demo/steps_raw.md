# Legend Demo Lab

## Introduction

In this lab, we will explore how to create and customize legends in Matplotlib. Legends are used to explain the meaning of the elements in a chart, including lines, bars, and markers. We will demonstrate how to create legends for specific lines, complex labels, and more complex plots. Finally, we will show how to write custom classes to stylize legends.

## Steps

### Step 1: Create a legend for specific lines

In this step, we will create a legend for specific lines.

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define data for the chart
t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.01)

# Create a plot with multiple lines
fig, ax = plt.subplots()
l1, = ax.plot(t2, np.exp(-t2))
l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 's-.')

# Create a legend for two of the lines
ax.legend((l2, l4), ('oscillatory', 'damped'), loc='upper right', shadow=True)

# Add labels and title to the chart
ax.set_xlabel('time')
ax.set_ylabel('volts')
ax.set_title('Damped oscillation')

# Display the chart
plt.show()
```

### Step 2: Plot more complex labels

In this step, we will plot more complex labels.

```python
# Define data for the chart
x = np.linspace(0, 1)

# Create a chart with multiple lines
fig, (ax0, ax1) = plt.subplots(2, 1)
for n in range(1, 5):
    ax0.plot(x, x**n, label=f"{n=}")

# Create a legend with multiple columns and a title
leg = ax0.legend(loc="upper left", bbox_to_anchor=[0, 1],
                 ncols=2, shadow=True, title="Legend", fancybox=True)
leg.get_title().set_color("red")

# Create a chart with multiple lines and markers
ax1.plot(x, x**2, label="multi\nline")
half_pi = np.linspace(0, np.pi / 2)
ax1.plot(np.sin(half_pi), np.cos(half_pi), label=r"$\frac{1}{2}\pi$")
ax1.plot(x, 2**(x**2), label="$2^{x^2}$")

# Create a legend with a shadow
ax1.legend(shadow=True, fancybox=True)

# Display the chart
plt.show()
```

### Step 3: Attach legends to more complex plots

In this step, we will attach legends to more complex plots.

```python
# Define data for the chart
fig, axs = plt.subplots(3, 1, layout="constrained")
top_ax, middle_ax, bottom_ax = axs

# Create a bar chart with multiple bars
top_ax.bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.4, label="Bar 1",
           align="center")
top_ax.bar([0.5, 1.5, 2.5], [0.3, 0.2, 0.2], color="red", width=0.4,
           label="Bar 2", align="center")
top_ax.legend()

# Create an error bar chart with multiple errors
middle_ax.errorbar([0, 1, 2], [2, 3, 1], xerr=0.4, fmt="s", label="test 1")
middle_ax.errorbar([0, 1, 2], [3, 2, 4], yerr=0.3, fmt="o", label="test 2")
middle_ax.errorbar([0, 1, 2], [1, 1, 3], xerr=0.4, yerr=0.3, fmt="^",
                   label="test 3")
middle_ax.legend()

# Create a stem chart with a legend
bottom_ax.stem([0.3, 1.5, 2.7], [1, 3.6, 2.7], label="stem test")
bottom_ax.legend()

# Display the chart
plt.show()
```

### Step 4: Create legend entries with more than one legend key

In this step, we will create legend entries with more than one legend key.

```python
# Define data for the chart
fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
p1 = ax1.scatter([1], [5], c='r', marker='s', s=100)
p2 = ax1.scatter([3], [2], c='b', marker='o', s=100)
p3, = ax1.plot([1, 5], [4, 4], 'm-d')

# Create a legend with two keys for one entry
l = ax1.legend([(p1, p3), p2], ['two keys', 'one key'], scatterpoints=1,
               numpoints=1, handler_map={tuple: HandlerTuple(ndivide=None)})

# Create two bar charts on top of each other and change the padding between the legend keys
x_left = [1, 2, 3]
y_pos = [1, 3, 2]
y_neg = [2, 1, 4]
rneg = ax2.bar(x_left, y_neg, width=0.5, color='w', hatch='///', label='-1')
rpos = ax2.bar(x_left, y_pos, width=0.5, color='k', label='+1')

# Treat each legend entry differently by using specific `HandlerTuple`s
l = ax2.legend([(rpos, rneg), (rneg, rpos)], ['pad!=0', 'pad=0'],
               handler_map={(rpos, rneg): HandlerTuple(ndivide=None),
                            (rneg, rpos): HandlerTuple(ndivide=None, pad=0.)})

# Display the chart
plt.show()
```

### Step 5: Write custom classes to stylize legends

In this step, we will write custom classes to stylize legends.

```python
# Define data for the chart
class HandlerDashedLines(HandlerLineCollection):
    """
    Custom Handler for LineCollection instances.
    """
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # figure out how many lines there are
        numlines = len(orig_handle.get_segments())
        xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                             width, height, fontsize)
        leglines = []
        # divide the vertical space where the lines will go
        # into equal parts based on the number of lines
        ydata = np.full_like(xdata, height / (numlines + 1))
        # for each line, create the line at the proper location
        # and set the dash pattern
        for i in range(numlines):
            legline = Line2D(xdata, ydata * (numlines - i) - ydescent)
            self.update_prop(legline, orig_handle, legend)
            # set color, dash pattern, and linewidth to that
            # of the lines in linecollection
            try:
                color = orig_handle.get_colors()[i]
            except IndexError:
                color = orig_handle.get_colors()[0]
            try:
                dashes = orig_handle.get_dashes()[i]
            except IndexError:
                dashes = orig_handle.get_dashes()[0]
            try:
                lw = orig_handle.get_linewidths()[i]
            except IndexError:
                lw = orig_handle.get_linewidths()[0]
            if dashes[1] is not None:
                legline.set_dashes(dashes[1])
            legline.set_color(color)
            legline.set_transform(trans)
            legline.set_linewidth(lw)
            leglines.append(legline)
        return leglines

# Create a chart with multiple lines
x = np.linspace(0, 5, 100)
fig, ax = plt.subplots()
colors = plt.rcParams['axes.prop_cycle'].by_key()['color'][:5]
styles = ['solid', 'dashed', 'dashed', 'dashed', 'solid']
for i, color, style in zip(range(5), colors, styles):
    ax.plot(x, np.sin(x) - .1 * i, c=color, ls=style)

# Create proxy artists and a legend
line = [[(0, 0)]]
lc = mcol.LineCollection(5 * line, linestyles=styles, colors=colors)
ax.legend([lc], ['multi-line'], handler_map={type(lc): HandlerDashedLines()},
          handlelength=2.5, handleheight=3)

# Display the chart
plt.show()
```

## Summary

In this lab, we learned how to create and customize legends in Matplotlib. We demonstrated how to create legends for specific lines, complex labels, and more complex plots. We also showed how to write custom classes to stylize legends. Legends are an important part of any chart, and understanding how to create and customize them is essential for creating effective visualizations.
