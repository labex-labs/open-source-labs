# Custom Mercator Latitude Scale in Matplotlib

## Introduction

Matplotlib is a powerful data visualization library for Python. It provides a number of built-in scales for plotting data, but sometimes you may need a custom scale for your specific use case. In this lab, we will show you how to create a custom scale that uses the Mercator projection for latitude data.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries.

```python
import numpy as np
from numpy import ma

from matplotlib import scale as mscale
from matplotlib import transforms as mtransforms
from matplotlib.ticker import FixedLocator, FuncFormatter
```

### Step 2: Define the MercatorLatitudeScale class

Next, we will define the `MercatorLatitudeScale` class that will implement the custom scale. This class will inherit from `mscale.ScaleBase`.

```python
class MercatorLatitudeScale(mscale.ScaleBase):
    """
    Scales data in range -pi/2 to pi/2 (-90 to 90 degrees) using
    the system used to scale latitudes in a Mercator__ projection.

    The scale function:
      ln(tan(y) + sec(y))

    The inverse scale function:
      atan(sinh(y))

    Since the Mercator scale tends to infinity at +/- 90 degrees,
    there is user-defined threshold, above and below which nothing
    will be plotted.  This defaults to +/- 85 degrees.

    __ https://en.wikipedia.org/wiki/Mercator_projection
    """
```

### Step 3: Implement the MercatorLatitudeTransform class

Inside the `MercatorLatitudeScale` class, we will define the `MercatorLatitudeTransform` class that will actually transform the data. This class will inherit from `mtransforms.Transform`.

```python
    class MercatorLatitudeTransform(mtransforms.Transform):
        # There are two value members that must be defined.
        # ``input_dims`` and ``output_dims`` specify number of input
        # dimensions and output dimensions to the transformation.
        # These are used by the transformation framework to do some
        # error checking and prevent incompatible transformations from
        # being connected together.  When defining transforms for a
        # scale, which are, by definition, separable and have only one
        # dimension, these members should always be set to 1.
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            """
            This transform takes a numpy array and returns a transformed copy.
            Since the range of the Mercator scale is limited by the
            user-specified threshold, the input array must be masked to
            contain only valid values.  Matplotlib will handle masked arrays
            and remove the out-of-range data from the plot.  However, the
            returned array *must* have the same shape as the input array, since
            these values need to remain synchronized with values in the other
            dimension.
            """
            masked = ma.masked_where((a < -self.thresh) | (a > self.thresh), a)
            if masked.mask.any():
                return ma.log(np.abs(ma.tan(masked) + 1 / ma.cos(masked)))
            else:
                return np.log(np.abs(np.tan(a) + 1 / np.cos(a)))

        def inverted(self):
            """
            Override this method so Matplotlib knows how to get the
            inverse transform for this transform.
            """
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform(
                self.thresh)
```

### Step 4: Implement the InvertedMercatorLatitudeTransform class

We will also define the `InvertedMercatorLatitudeTransform` class that will be used to get the inverse transform for this scale.

```python
    class InvertedMercatorLatitudeTransform(mtransforms.Transform):
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            return np.arctan(np.sinh(a))

        def inverted(self):
            return MercatorLatitudeScale.MercatorLatitudeTransform(self.thresh)
```

### Step 5: Register the custom scale

We will register the custom scale with Matplotlib using `mscale.register_scale`.

```python
mscale.register_scale(MercatorLatitudeScale)
```

### Step 6: Use the custom scale

Now we can use the custom scale in our plots. Here's an example of using the custom scale for latitude data in a Mercator projection.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    t = np.arange(-180.0, 180.0, 0.1)
    s = np.radians(t)/2.

    plt.plot(t, s, '-', lw=2)
    plt.yscale('mercator')

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Mercator projection')
    plt.grid(True)

    plt.show()
```

## Summary

In this lab, we learned how to create a custom scale in Matplotlib using the Mercator projection for latitude data. We defined the `MercatorLatitudeScale` and `MercatorLatitudeTransform` classes and registered the custom scale with Matplotlib using `mscale.register_scale`. We also showed an example of using the custom scale for latitude data in a Mercator projection.
