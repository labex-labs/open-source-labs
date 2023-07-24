# Matplotlib Date Precision and Epochs Lab

## Introduction

This is a step-by-step lab that demonstrates how to handle date precision and epochs in Matplotlib. Matplotlib can work with `.datetime` objects and `numpy.datetime64` objects using a unit converter that recognizes these dates and converts them to floating point numbers. Before Matplotlib 3.3, the default for this conversion returns a float that was days since "0000-12-31T00:00:00". As of Matplotlib 3.3, the default is days from "1970-01-01T00:00:00". This allows more resolution for modern dates.

## Steps

### Step 1: Import necessary packages

The first step is to import the necessary packages, including `datetime`, `matplotlib.pyplot`, and `numpy`.

```python
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
```

### Step 2: Set epoch to the old default

The next step is to set the epoch to the old default, which is days since "0000-12-31T00:00:00". This is done using the `mdates.set_epoch` method.

```python
mdates.set_epoch('0000-12-31T00:00:00')
```

### Step 3: Convert datetime to matplotlib date

Now that the epoch has been set, we can convert a `datetime` object to a Matplotlib date using the `mdates.date2num` function.

```python
date1 = datetime.datetime(2000, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```

### Step 4: Round-trip the date

We can then round-trip the date using the `mdates.num2date` function to make sure the conversion is accurate.

```python
date2 = mdates.num2date(mdate1)
```

### Step 5: Set epoch to the new default

To use modern dates at microsecond precision, we need to set the epoch to the new default, which is days since "1970-01-01T00:00:00".

```python
mdates.set_epoch('1970-01-01T00:00:00')
```

### Step 6: Convert datetime to matplotlib date with new epoch

Now that the epoch has been set to the new default, we can convert a `datetime` object to a Matplotlib date using the `mdates.date2num` function.

```python
date1 = datetime.datetime(2020, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```

### Step 7: Round-trip the date with new epoch

We can then round-trip the date using the `mdates.num2date` function to make sure the conversion is accurate.

```python
date2 = mdates.num2date(mdate1)
```

### Step 8: Convert numpy.datetime64 to matplotlib date

`numpy.datetime64` objects have microsecond precision for a much larger timespace than `.datetime` objects. However, currently, Matplotlib time is only converted back to datetime objects, which have microsecond resolution and years that only span 0000 to 9999.

```python
date1 = np.datetime64('2000-01-01T00:10:00.000012')
mdate1 = mdates.date2num(date1)
```

### Step 9: Plotting

This step demonstrates how the epoch affects plotting. With the old default epoch, the times were rounded during the internal `date2num` conversion, leading to jumps in the data.

```python
mdates.set_epoch('0000-12-31T00:00:00')

x = np.arange('2000-01-01T00:00:00.0', '2000-01-01T00:00:00.000100', dtype='datetime64[us]')
xold = np.array([mdates.num2date(mdates.date2num(d)) for d in x])
y = np.arange(0, len(x))

fig, ax = plt.subplots(layout='constrained')
ax.plot(xold, y)
ax.set_title('Epoch: ' + mdates.get_epoch())
ax.xaxis.set_tick_params(rotation=40)
plt.show()
```

For dates plotted using the more recent epoch, the plot is smooth:

```python
mdates.set_epoch('1970-01-01T00:00:00')

fig, ax = plt.subplots(layout='constrained')
ax.plot(x, y)
ax.set_title('Epoch: ' + mdates.get_epoch())
ax.xaxis.set_tick_params(rotation=40)
plt.show()
```

## Summary

This lab demonstrates how to handle date precision and epochs in Matplotlib. We can set the epoch to the old default or the new default using the `mdates.set_epoch` method. We can then convert `datetime` or `numpy.datetime64` objects to Matplotlib dates using the `mdates.date2num` function, and round-trip the dates using the `mdates.num2date` function to make sure the conversion is accurate. We can also plot data with different epochs to observe the differences in the plot.
