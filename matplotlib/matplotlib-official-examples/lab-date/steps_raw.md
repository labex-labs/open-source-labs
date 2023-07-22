# Python Matplotlib Date Plotting Lab

## Introduction

In this lab, we will learn how to create date plots using Matplotlib in Python. We will use the `matplotlib.dates` module to convert datetime objects to Matplotlib's internal representation. We will also learn how to format the tick labels on the x-axis to display dates in a readable format.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries, including `matplotlib.pyplot`, `matplotlib.cbook`, and `matplotlib.dates`.

```python
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
```

### Step 2: Load data

Next, we will load the data that we want to plot. We will use a numpy record array from Yahoo csv data with fields date, open, high, low, close, volume, adj_close from the mpl-data/sample_data directory. The record array stores the date as an np.datetime64 with a day unit ('D') in the date column.

```python
data = cbook.get_sample_data('goog.npz')['price_data']
```

### Step 3: Create subplots

We will create three subplots to show different formatting options for the tick labels.

```python
fig, axs = plt.subplots(3, 1, figsize=(6.4, 7), layout='constrained')
```

### Step 4: Plot data

We will plot the data on all three subplots using the `plot` function.

```python
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    ax.grid(True)
    ax.set_ylabel(r'Price [\$]')
```

### Step 5: Format tick labels using default formatter

We will format the tick labels on the first subplot using the default formatter.

```python
ax = axs[0]
ax.set_title('DefaultFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
```

### Step 6: Format tick labels using concise formatter

We will format the tick labels on the second subplot using the concise formatter.

```python
ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
```

### Step 7: Format tick labels manually

We will format the tick labels on the third subplot manually using `DateFormatter` to format the dates using the format strings documented at `datetime.date.strftime`.

```python
ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
```

### Step 8: Display plot

Finally, we will display the plot using the `show` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create date plots using Matplotlib in Python. We used the `matplotlib.dates` module to convert datetime objects to Matplotlib's internal representation. We also learned how to format the tick labels on the x-axis to display dates in a readable format.
