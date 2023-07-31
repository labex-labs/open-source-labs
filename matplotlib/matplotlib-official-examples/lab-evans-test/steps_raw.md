# Matplotlib Custom Units Lab

## Introduction

Matplotlib is a plotting library for the Python programming language. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. Matplotlib allows developers to create a wide range of static, animated, and interactive visualizations in Python.

In this lab, we will learn how to create custom units in Matplotlib and plot data using these custom units.

## Steps

### Step 1: Import Libraries

In the first step, we need to import the required libraries - `matplotlib.pyplot`, `numpy`, `matplotlib.ticker`, and `matplotlib.units`.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.units as units
```

### Step 2: Create a Custom Unit Class

In this step, we will create a custom unit class - `Foo`. This class will support conversion and different tick formatting depending on the "unit". Here, the "unit" is just a scalar conversion factor.

```python
class Foo:
    def __init__(self, val, unit=1.0):
        self.unit = unit
        self._val = val * unit

    def value(self, unit):
        if unit is None:
            unit = self.unit
        return self._val / unit
```

### Step 3: Create a Converter Class

In this step, we will create a converter class - `FooConverter`. This class will define three static methods - `axisinfo`, `convert`, and `default_units`.

```python
class FooConverter(units.ConversionInterface):
    @staticmethod
    def axisinfo(unit, axis):
        """Return the Foo AxisInfo."""
        if unit == 1.0 or unit == 2.0:
            return units.AxisInfo(
                majloc=ticker.IndexLocator(8, 0),
                majfmt=ticker.FormatStrFormatter("VAL: %s"),
                label='foo',
                )

        else:
            return None

    @staticmethod
    def convert(obj, unit, axis):
        """
        Convert *obj* using *unit*.

        If *obj* is a sequence, return the converted sequence.
        """
        if np.iterable(obj):
            return [o.value(unit) for o in obj]
        else:
            return obj.value(unit)

    @staticmethod
    def default_units(x, axis):
        """Return the default unit for *x* or None."""
        if np.iterable(x):
            for thisx in x:
                return thisx.unit
        else:
            return x.unit
```

### Step 4: Register the Custom Unit Class

In this step, we will register the custom unit class - `Foo` - with the converter class - `FooConverter`.

```python
units.registry[Foo] = FooConverter()
```

### Step 5: Create Data Points

In this step, we will create some data points using the custom unit class - `Foo`.

```python
# create some Foos
x = [Foo(val, 1.0) for val in range(0, 50, 2)]
# and some arbitrary y data
y = [i for i in range(len(x))]
```

### Step 6: Create Plots

In this step, we will create two plots - one using custom units and the other using default units.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Custom units")
fig.subplots_adjust(bottom=0.2)

# plot specifying units
ax2.plot(x, y, 'o', xunits=2.0)
ax2.set_title("xunits = 2.0")
plt.setp(ax2.get_xticklabels(), rotation=30, ha='right')

# plot without specifying units; will use the None branch for axisinfo
ax1.plot(x, y)  # uses default units
ax1.set_title('default units')
plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

plt.show()
```

### Step 7: Run the Code

In the final step, run the code to create the custom unit plots.

## Summary

In this lab, we learned how to create custom units in Matplotlib using a custom unit class and a converter class. We then created two plots - one using custom units and the other using default units - to demonstrate the usage of these custom units. Custom units can be useful when dealing with complex data that requires custom scaling or tick formatting.
