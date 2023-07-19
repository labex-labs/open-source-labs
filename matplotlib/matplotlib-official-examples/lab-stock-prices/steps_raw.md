# Python Matplotlib Tutorial

## Introduction

In this lab, you will learn how to create a graph of multiple time series that demonstrates custom styling of plot frame, tick lines, tick labels, and line graph properties using Matplotlib. The graph will display stock prices of various companies over a period of 32 years.

## Steps

### Step 1: Import necessary libraries

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data
import matplotlib.transforms as mtransforms
```

### Step 2: Load the stock data

```python
with get_sample_data('Stocks.csv') as file:
    stock_data = np.genfromtxt(
        file, delimiter=',', names=True, dtype=None,
        converters={0: lambda x: np.datetime64(x, 'D')}, skip_header=1)
```

### Step 3: Create a figure and axis object

```python
fig, ax = plt.subplots(1, 1, figsize=(6, 8), layout='constrained')
```

### Step 4: Define the colors to be used in the plot

```python
ax.set_prop_cycle(color=[
    '#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a',
    '#d62728', '#ff9896', '#9467bd', '#c5b0d5', '#8c564b', '#c49c94',
    '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d',
    '#17becf', '#9edae5'])
```

### Step 5: Set the names and tickers of the stocks to be plotted

```python
stocks_name = ['IBM', 'Apple', 'Microsoft', 'Xerox', 'Amazon', 'Dell',
               'Alphabet', 'Adobe', 'S&P 500', 'NASDAQ']
stocks_ticker = ['IBM', 'AAPL', 'MSFT', 'XRX', 'AMZN', 'DELL', 'GOOGL',
                 'ADBE', 'GSPC', 'IXIC']
```

### Step 6: Manually adjust the label positions vertically to avoid overlapping

```python
y_offsets = {k: 0 for k in stocks_ticker}
y_offsets['IBM'] = 5
y_offsets['AAPL'] = -5
y_offsets['AMZN'] = -6
```

### Step 7: Plot each stock separately with its own color

```python
for nn, column in enumerate(stocks_ticker):
    # Plot each line separately with its own color.
    # don't include any data with NaN.
    good = np.nonzero(np.isfinite(stock_data[column]))
    line, = ax.plot(stock_data['Date'][good], stock_data[column][good], lw=2.5)

    # Add a text label to the right end of every line. Most of the code below
    # is adding specific offsets y position because some labels overlapped.
    y_pos = stock_data[column][-1]

    # Use an offset transform, in points, for any text that needs to be nudged
    # up or down.
    offset = y_offsets[column] / 72
    trans = mtransforms.ScaledTranslation(0, offset, fig.dpi_scale_trans)
    trans = ax.transData + trans

    # Again, make sure that all labels are large enough to be easily read
    # by the viewer.
    ax.text(np.datetime64('2022-10-01'), y_pos, stocks_name[nn],
            color=line.get_color(), transform=trans)
```

### Step 8: Set the limits of the x-axis and y-axis, and add title and grid

```python
ax.set_xlim(np.datetime64('1989-06-01'), np.datetime64('2023-01-01'))
fig.suptitle("Technology company stocks prices dollars (1990-2022)", ha="center")
ax.spines[:].set_visible(False)
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
ax.set_yscale('log')
ax.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
ax.tick_params(axis='both', which='both', labelsize='large',
               bottom=False, top=False, labelbottom=True,
               left=False, right=False, labelleft=True)
```

### Step 9: Display the graph

```python
plt.show()
```

## Summary

In this lab, you learned how to create a graph of multiple time series that demonstrates custom styling of plot frame, tick lines, tick labels, and line graph properties using Matplotlib. You also learned how to plot each stock separately with its own color, set the limits of the x-axis and y-axis, and add title and grid.
