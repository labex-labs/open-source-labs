# Python Matplotlib Tutorial - Date Tick Locators and Formatters

## Introduction

This lab aims to provide an understanding of how to use the various date tick locators and formatters in Matplotlib. This tutorial demonstrates how to use these functions to customize the X-axis of a plot with time-based data.

## Steps

### Step 1: Importing Required Libraries

We begin by importing the necessary libraries for this tutorial. We will be using `matplotlib` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import (
    FR, MO, MONTHLY, SA, SU, TH, TU, WE, AutoDateFormatter, AutoDateLocator,
    ConciseDateFormatter, DateFormatter, DayLocator, HourLocator,
    MicrosecondLocator, MinuteLocator, MonthLocator, RRuleLocator, SecondLocator,
    WeekdayLocator, YearLocator, rrulewrapper)
import matplotlib.ticker as ticker
```

### Step 2: Defining the Locators and Formatters

We define the various locators and formatters that we will be using. This example uses the following locators:

- `AutoDateLocator(maxticks=8)`
- `YearLocator(month=4)`
- `MonthLocator(bymonth=[4, 8, 12])`
- `DayLocator(interval=180)`
- `WeekdayLocator(byweekday=SU, interval=4)`
- `HourLocator(byhour=range(0, 24, 6))`
- `MinuteLocator(interval=15)`
- `SecondLocator(bysecond=(0, 30))`
- `MicrosecondLocator(interval=1000)`
- `RRuleLocator(rrulewrapper(freq=MONTHLY, byweekday=(MO, TU, WE, TH, FR), bysetpos=-1))`

And the following formatters:

- `AutoDateFormatter(ax.xaxis.get_major_locator())`
- `ConciseDateFormatter(ax.xaxis.get_major_locator())`
- `DateFormatter("%b %Y")`

```python
locators = [
    ('AutoDateLocator(maxticks=8)', '2003-02-01', '%Y-%m'),
    ('YearLocator(month=4)', '2003-02-01', '%Y-%m'),
    ('MonthLocator(bymonth=[4, 8, 12])', '2003-02-01', '%Y-%m'),
    ('DayLocator(interval=180)', '2003-02-01', '%Y-%m-%d'),
    ('WeekdayLocator(byweekday=SU, interval=4)', '2000-07-01', '%a %Y-%m-%d'),
    ('HourLocator(byhour=range(0, 24, 6))', '2000-02-04', '%H h'),
    ('MinuteLocator(interval=15)', '2000-02-01 02:00', '%H:%M'),
    ('SecondLocator(bysecond=(0, 30))', '2000-02-01 00:02', '%H:%M:%S'),
    ('MicrosecondLocator(interval=1000)', '2000-02-01 00:00:00.005', '%S.%f'),
    ('RRuleLocator(rrulewrapper(freq=MONTHLY, byweekday=(MO, TU, WE, TH, FR), '
     'bysetpos=-1))', '2000-07-01', '%Y-%m-%d'),
]

formatters = [
    'AutoDateFormatter(ax.xaxis.get_major_locator())',
    'ConciseDateFormatter(ax.xaxis.get_major_locator())',
    'DateFormatter("%b %Y")',
]
```

### Step 3: Plotting the Graphs

Now, we can create our plots. We will create two subplots to demonstrate the locators and formatters separately. For each locator and formatter, we plot a graph that shows how it affects the X-axis. We use the `plot_axis` function to do this. This function sets up the common parameters for each axis, such as the spines, tick parameters, and limits. It also sets the locator and formatter for the X-axis.

```python
def plot_axis(ax, locator=None, xmax='2002-02-01', fmt=None, formatter=None):
    ax.spines[['left', 'right', 'top']].set_visible(False)
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xlim(np.datetime64('2000-02-01'), np.datetime64(xmax))
    if locator:
        ax.xaxis.set_major_locator(eval(locator))
        ax.xaxis.set_major_formatter(DateFormatter(fmt))
    else:
        ax.xaxis.set_major_formatter(eval(formatter))
    ax.text(0.0, 0.2, locator or formatter, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


fig, axs = plt.subplots(len(locators), 1, figsize=(8, len(locators) * .8),
                        layout='constrained')
fig.suptitle('Date Locators')
for ax, (locator, xmax, fmt) in zip(axs, locators):
    plot_axis(ax, locator, xmax, fmt)

fig, axs = plt.subplots(len(formatters), 1, figsize=(8, len(formatters) * .8),
                        layout='constrained')
fig.suptitle('Date Formatters')
for ax, fmt in zip(axs, formatters):
    plot_axis(ax, formatter=fmt)
```

### Step 4: Displaying the Graphs

Finally, we can display the graphs using the `plt.show()` function.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to use the various date tick locators and formatters in Matplotlib. We plotted several graphs that demonstrated how each locator and formatter affects the X-axis of a plot with time-based data. This knowledge can be useful when creating visualizations of time series data.
