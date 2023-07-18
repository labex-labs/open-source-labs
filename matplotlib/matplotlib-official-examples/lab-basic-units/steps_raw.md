# Basic Units Conversion Lab

## Introduction

In scientific calculations, it is important to keep track of the units of measurement. The `BasicUnit` class and `TaggedValue` class in this lab provide a convenient way to represent values with units and perform unit conversions. In this lab, you will learn how to use these classes to perform basic unit conversions and use them with Matplotlib.

## Steps

### Step 1: Create Basic Units

The `BasicUnit` class is used to represent units of measurement. In this step, you will create some basic units and define conversion factors between them.

```python
cm = BasicUnit('cm', 'centimeters')
inch = BasicUnit('inch', 'inches')
inch.add_conversion_factor(cm, 2.54)
cm.add_conversion_factor(inch, 1/2.54)

radians = BasicUnit('rad', 'radians')
degrees = BasicUnit('deg', 'degrees')
radians.add_conversion_factor(degrees, 180.0/np.pi)
degrees.add_conversion_factor(radians, np.pi/180.0)

secs = BasicUnit('s', 'seconds')
hertz = BasicUnit('Hz', 'Hertz')
minutes = BasicUnit('min', 'minutes')

secs.add_conversion_fn(hertz, lambda x: 1./x)
secs.add_conversion_factor(minutes, 1/60.0)
```

### Step 2: Create Tagged Values

The `TaggedValue` class is used to represent values with units. In this step, you will create some tagged values.

```python
length = 10 * cm
time = 5 * secs
freq = 2 * hertz
```

### Step 3: Perform Unit Conversions

Unit conversions can be performed using the `convert_to` method of `TaggedValue`.

```python
# convert cm to inch
print(length.convert_to(inch))

# convert radians to degrees
print(radians.convert_to(degrees))

# convert seconds to minutes
print(time.convert_to(minutes))
```

### Step 4: Perform Basic Calculations

Basic calculations can be performed with tagged values using standard operators.

```python
# addition and subtraction
print(length + 5 * inch)
print(time - 2 * secs)

# multiplication and division
print(length * 2)
print(time / 2)
```

### Step 5: Use Tagged Values with Matplotlib

Matplotlib can be used with tagged values by registering a custom converter. In this step, you will create a custom converter for radians.

```python
def rad_fn(x, pos=None):
    if x >= 0:
        n = int((x / np.pi) * 2.0 + 0.25)
    else:
        n = int((x / np.pi) * 2.0 - 0.25)

    if n == 0:
        return '0'
    elif n == 1:
        return r'$\pi/2$'
    elif n == 2:
        return r'$\pi$'
    elif n == -1:
        return r'$-\pi/2$'
    elif n == -2:
        return r'$-\pi$'
    elif n % 2 == 0:
        return fr'${n//2}\pi$'
    else:
        return fr'${n}\pi/2$'


class BasicUnitConverter(units.ConversionInterface):
    @staticmethod
    def axisinfo(unit, axis):
        if unit == radians:
            return units.AxisInfo(
                majloc=ticker.MultipleLocator(base=np.pi/2),
                majfmt=ticker.FuncFormatter(rad_fn),
                label=unit.fullname,
            )
        elif unit == degrees:
            return units.AxisInfo(
                majloc=ticker.AutoLocator(),
                majfmt=ticker.FormatStrFormatter(r'$%i^\circ$'),
                label=unit.fullname,
            )
        elif unit is not None:
            if hasattr(unit, 'fullname'):
                return units.AxisInfo(label=unit.fullname)
            elif hasattr(unit, 'unit'):
                return units.AxisInfo(label=unit.unit.fullname)
        return None

    @staticmethod
    def convert(val, unit, axis):
        if np.iterable(val):
            if isinstance(val, np.ma.MaskedArray):
                val = val.astype(float).filled(np.nan)
            out = np.empty(len(val))
            for i, thisval in enumerate(val):
                if np.ma.is_masked(thisval):
                    out[i] = np.nan
                else:
                    try:
                        out[i] = thisval.convert_to(unit).get_value()
                    except AttributeError:
                        out[i] = thisval
            return out
        if np.ma.is_masked(val):
            return np.nan
        else:
            return val.convert_to(unit).get_value()

    @staticmethod
    def default_units(x, axis):
        if np.iterable(x):
            for thisx in x:
                return thisx.unit
        return x.unit


# register the converter
units.registry[BasicUnit] = units.registry[TaggedValue] = BasicUnitConverter()

# plot a sine wave with radians
x = np.linspace(-2*np.pi, 2*np.pi)
y = np.sin(x * radians)
plt.plot(x, y)
plt.xlabel('Angle')
plt.ylabel('sin(x)')
plt.show()
```

## Summary

In this lab, you learned how to use the `BasicUnit` and `TaggedValue` classes to perform basic unit conversions and use them with Matplotlib. By keeping track of units of measurement, you can ensure the accuracy and consistency of your calculations.
