# Matplotlib Tutorial: Centering Labels between Ticks

## Introduction

In this lab, we will learn how to center labels between ticks in a Matplotlib plot using Python. By default, tick labels are aligned relative to their associated tick, but there is no direct way to center the labels between ticks. However, we can place a label on the minor ticks in between the major ticks and hide the major tick labels and minor ticks to fake this behavior. We will use financial data for Google's stock price to demonstrate this technique.

## Steps

### Step 1: Load the Financial Data

First, we need to load some financial data for Google's stock price using the Matplotlib `cbook.get_sample_data()` function. We will use the last 250 days of data.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Load some financial data; Google's stock price
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # get the last 250 days
```

### Step 2: Create the Plot

Next, we will create the plot using Matplotlib's `subplots()` function and plot the adjusted close price of Google's stock over time.

```python
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
```

### Step 3: Set the Major and Minor Locators and Formatters

To center the labels between ticks, we need to set the major and minor locators and formatters for the x-axis. We will use the `dates.MonthLocator()` function to set the major and minor locators to the month and the `dates.DateFormatter()` function to format the minor tick labels to the month abbreviation.

```python
import matplotlib.dates as dates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16 is a slight approximation since months differ in number of days.
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
```

### Step 4: Remove the Major Tick Labels and Minor Ticks

To fake the behavior of centering the labels between ticks, we need to remove the major tick labels and minor ticks and only show the minor tick labels. We can do this using the `tick_params()` function and setting the `tick1On` and `tick2On` parameters to `False`.

```python
# Remove the tick lines
ax.tick_params(axis='x', which='minor', tick1On=False, tick2On=False)
```

### Step 5: Align the Minor Tick Labels

Finally, we need to align the minor tick labels to the center between the major ticks. We can do this using the `get_xticklabels()` function and setting the `minor` parameter to `True` to get the minor tick labels. We can then loop through the labels and set the horizontal alignment to `'center'`.

```python
# Align the minor tick label
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment('center')
imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))
```

### Step 6: Show the Plot

We can now show the plot using the `show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to center labels between ticks in a Matplotlib plot using Python. We used financial data for Google's stock price to demonstrate this technique and followed the following steps:

1. Loaded the financial data
2. Created the plot
3. Set the major and minor locators and formatters
4. Removed the major tick labels and minor ticks
5. Aligned the minor tick labels to the center between the major ticks
6. Showed the plot.
