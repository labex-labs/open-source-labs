# Step-by-Step Lab: Using Recurrence Rules in Matplotlib to Place Date Ticks

## Introduction

In this lab, you will learn how to use recurrence rules in Matplotlib to place date ticks. The `iCalender RFC`\_ specifies recurrence rules (rrules), that define date sequences. You can use rrules in Matplotlib to place date ticks. This example sets custom date ticks on every 5th Easter.

## Steps

### Step 1: Import the necessary libraries

First, you need to import the necessary libraries, including Matplotlib, NumPy, and datetime.

```python
import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import (YEARLY, DateFormatter, RRuleLocator, drange,
                              rrulewrapper)
```

### Step 2: Set the random seed

You will be generating random data for this example, so you need to set the random seed for reproducibility.

```python
np.random.seed(19680801)
```

### Step 3: Set the recurrence rule

You will be setting custom date ticks on every 5th Easter. To do this, you need to set the recurrence rule using the rrulewrapper function.

```python
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
```

### Step 4: Set the tick locator and formatter

You will use the RRuleLocator function to set the tick locator based on the recurrence rule you set in the previous step. You will also use the DateFormatter function to set the tick formatter.

```python
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
```

### Step 5: Set the dates and generate random data

You need to set the start and end dates and the delta, which represents the difference between each date. You also need to generate random data for the example.

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```

### Step 6: Plot the data and set the x-axis ticks

Finally, you can plot the data using the plot function, and set the x-axis ticks using the tick locator and formatter functions you set earlier.

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```

## Summary

In this lab, you learned how to use recurrence rules in Matplotlib to place custom date ticks on a plot. You first set the recurrence rule using the rrulewrapper function, and then used the RRuleLocator and DateFormatter functions to set the tick locator and formatter. Finally, you plotted the data and set the x-axis ticks using the tick locator and formatter functions.
