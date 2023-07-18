# Custom Tick Formatter for Time Series

## Introduction

When plotting daily data such as financial time series, one often wants to leave out days on which there is no data, such as weekends. This allows the data to be plotted at regular intervals without extra spaces for the days with no data. In this lab, we will learn how to use an 'index formatter' to achieve the desired plot.

## Steps

### Step 1: Import Required Libraries and Data

We first need to import the required libraries, which are `matplotlib`, `numpy`, and `matplotlib.cbook`. We also need to load a numpy record array from yahoo csv data with fields date, open, high, low, close, volume, adj_close from the mpl-data/sample_data directory. The record array stores the date as an np.datetime64 with a day unit ('D') in the date column. We will use this data to plot the financial time series.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Load data from sample_data directory
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[:9]  # get the first 9 days
```

### Step 2: Plotting Data with Default Gaps on Weekends

We will first plot the data with the default gaps on weekends using the `plot` function in matplotlib. We will also highlight gaps in the daily data using white dashed lines.

```python
# Plot data with gaps on weekends
fig, ax1 = plt.subplots(figsize=(6, 3))
ax1.plot(r.date, r.adj_close, 'o-')

# Highlight gaps in daily data
gaps = np.flatnonzero(np.diff(r.date) > np.timedelta64(1, 'D'))
for gap in r[['date', 'adj_close']][np.stack((gaps, gaps + 1)).T]:
    ax1.plot(gap.date, gap.adj_close, 'w--', lw=2)
ax1.legend(handles=[ml.Line2D([], [], ls='--', label='Gaps in daily data')])

ax1.set_title("Plotting Data with Default Gaps on Weekends")
ax1.xaxis.set_major_locator(DayLocator())
ax1.xaxis.set_major_formatter(DateFormatter('%a'))
```

### Step 3: Creating Custom Index Formatter

To plot the data against an index that goes from 0, 1, ... len(data), we will create a custom index formatter. This formatter will format the tick marks as times instead of integers.

```python
# Create custom index formatter
fig, ax2 = plt.subplots(figsize=(6, 3))
ax2.plot(r.adj_close, 'o-')

# Format x-axis as times
def format_date(x, _):
    try:
        # convert datetime64 to datetime, and use datetime's strftime:
        return r.date[round(x)].item().strftime('%a')
    except IndexError:
        pass

ax2.set_title("Creating Custom Index Formatter")
ax2.xaxis.set_major_formatter(format_date)  # internally creates FuncFormatter
```

### Step 4: Using a Callable for Formatter

Instead of passing a function into `.Axis.set_major_formatter`, we can use any other callable, such as an instance of a class that implements `__call__`. In this step, we will create a class `MyFormatter` that formats the tick marks as times.

```python
# Use a callable for formatter
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%a'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        """Return the label for time x at position pos."""
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass

ax2.xaxis.set_major_formatter(MyFormatter(r.date, '%a'))
```

### Step 5: Displaying the Plot

We will now display the plot using the `show` function in matplotlib.

```python
plt.show()
```

## Summary

In this lab, we learned how to use a custom index formatter to plot financial time series without gaps on weekends. We also learned how to use a callable for the formatter instead of a function. By using these techniques, we can create more visually appealing plots of daily data.
