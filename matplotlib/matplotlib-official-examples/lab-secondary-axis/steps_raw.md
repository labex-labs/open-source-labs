# Matplotlib Secondary Axis Lab

## Introduction

Matplotlib is a popular data visualization library in Python. Sometimes, we need to plot two different scales of data on the same graph, this is when the concept of a secondary axis comes into play. In this lab, we will learn how to create a secondary axis in Matplotlib.

## Steps

### Step 1: Import the necessary libraries

We will start by importing the necessary libraries, which are `matplotlib`, `numpy`, and `datetime`.

```python
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.ticker import AutoMinorLocator
```

### Step 2: Plot the data

We will create a simple sine wave to demonstrate the use of a secondary axis. We will plot the sine wave using degrees as the x-axis.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 360, 1)
y = np.sin(2 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('angle [degrees]')
ax.set_ylabel('signal')
ax.set_title('Sine wave')
```

### Step 3: Create the Secondary Axis

We will now create the secondary axis and convert the x-axis from degrees to radians. We will use `deg2rad` as the forward function and `rad2deg` as the inverse function.

```python
def deg2rad(x):
    return x * np.pi / 180

def rad2deg(x):
    return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('angle [rad]')
```

### Step 4: Plot another example

We will now plot another example of converting from wavenumber to wavelength in a log-log scale. We will use a random spectrum for this example.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0.02, 1, 0.02)
np.random.seed(19680801)
y = np.random.randn(len(x)) ** 2
ax.loglog(x, y)
ax.set_xlabel('f [Hz]')
ax.set_ylabel('PSD')
ax.set_title('Random spectrum')
```

### Step 5: Create the Secondary X-Axis

We will create the secondary x-axis and convert from frequency to period. We will use `one_over` as the forward function and `inverse` as the inverse function.

```python
def one_over(x):
    """Vectorized 1/x, treating x==0 manually"""
    x = np.array(x, float)
    near_zero = np.isclose(x, 0)
    x[near_zero] = np.inf
    x[~near_zero] = 1 / x[~near_zero]
    return x

# the function "1/x" is its own inverse
inverse = one_over

secax = ax.secondary_xaxis('top', functions=(one_over, inverse))
secax.set_xlabel('period [s]')
```

### Step 6: Create the Secondary Y-Axis

We will create a third example of relating the axes in a transform that is ad-hoc from the data, and is derived empirically. In this case, we will set the forward and inverse transforms functions to be linear interpolations from the one data set to the other.

```python
fig, ax = plt.subplots(layout='constrained')
xdata = np.arange(1, 11, 0.4)
ydata = np.random.randn(len(xdata))
ax.plot(xdata, ydata, label='Plotted data')

xold = np.arange(0, 11, 0.2)
# fake data set relating x coordinate to another data-derived coordinate.
# xnew must be monotonic, so we sort...
xnew = np.sort(10 * np.exp(-xold / 4) + np.random.randn(len(xold)) / 3)

ax.plot(xold[3:], xnew[3:], label='Transform data')
ax.set_xlabel('X [m]')
ax.legend()

def forward(x):
    return np.interp(x, xold, xnew)

def inverse(x):
    return np.interp(x, xnew, xold)

secax = ax.secondary_xaxis('top', functions=(forward, inverse))
secax.xaxis.set_minor_locator(AutoMinorLocator())
secax.set_xlabel('$X_{other}$')
```

### Step 7: Create Multiple Axes

We will now create a final example that translates `np.datetime64` to yearday on the x-axis and from Celsius to Fahrenheit on the y-axis. We will also add a third y-axis and place it using a float for the location argument.

```python
dates = [datetime.datetime(2018, 1, 1) + datetime.timedelta(hours=k * 6)
         for k in range(240)]
temperature = np.random.randn(len(dates)) * 4 + 6.7
fig, ax = plt.subplots(layout='constrained')

ax.plot(dates, temperature)
ax.set_ylabel(r'$T\ [^oC]$')
plt.xticks(rotation=70)

def date2yday(x):
    """Convert matplotlib datenum to days since 2018-01-01."""
    y = x - mdates.date2num(datetime.datetime(2018, 1, 1))
    return y

def yday2date(x):
    """Return a matplotlib datenum for *x* days after 2018-01-01."""
    y = x + mdates.date2num(datetime.datetime(2018, 1, 1))
    return y

secax_x = ax.secondary_xaxis('top', functions=(date2yday, yday2date))
secax_x.set_xlabel('yday [2018]')

def celsius_to_fahrenheit(x):
    return x * 1.8 + 32

def fahrenheit_to_celsius(x):
    return (x - 32) / 1.8

secax_y = ax.secondary_yaxis(
    'right', functions=(celsius_to_fahrenheit, fahrenheit_to_celsius))
secax_y.set_ylabel(r'$T\ [^oF]$')

def celsius_to_anomaly(x):
    return (x - np.mean(temperature))

def anomaly_to_celsius(x):
    return (x + np.mean(temperature))

# use of a float for the position:
secax_y2 = ax.secondary_yaxis(
    1.2, functions=(celsius_to_anomaly, anomaly_to_celsius))
secax_y2.set_ylabel(r'$T - \overline{T}\ [^oC]$')
```

## Summary

In this lab, we learned how to create a secondary axis in Matplotlib. We used various examples to demonstrate the concept of a secondary axis and how to create it.
