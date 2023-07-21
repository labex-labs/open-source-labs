# Matplotlib Color Vision Deficiency Simulation Lab

## Introduction

Matplotlib is a popular data visualization library in Python. It has various built-in features, including the ability to simulate color vision deficiencies. This lab will guide you through the steps of using Matplotlib to simulate color vision deficiencies.

## Steps

### Step 1: Import necessary libraries and modules

First, we need to import the necessary libraries and modules, including Matplotlib, NumPy, and colorspacious. We also set the color filter options that we want to simulate.

```python
import functools
from pathlib import Path

import colorspacious

import numpy as np

_BUTTON_NAME = "Filter"
_BUTTON_HELP = "Simulate color vision deficiencies"
_MENU_ENTRIES = {
    "None": None,
    "Greyscale": "greyscale",
    "Deuteranopia": "deuteranomaly",
    "Protanopia": "protanomaly",
    "Tritanopia": "tritanomaly",
}
```

### Step 2: Define the color filter function

Next, we define a function that creates a color filter function based on the color filter name. This function uses the colorspacious module to convert the input image to a different color space based on the color filter name.

```python
def _get_color_filter(name):
    """
    Given a color filter name, create a color filter function.

    Parameters
    ----------
    name : str
        The color filter name, one of the following:

        - ``"none"``: ...
        - ``"greyscale"``: Convert the input to luminosity.
        - ``"deuteranopia"``: Simulate the most common form of red-green
          colorblindness.
        - ``"protanopia"``: Simulate a rarer form of red-green colorblindness.
        - ``"tritanopia"``: Simulate the rare form of blue-yellow
          colorblindness.

        Color conversions use `colorspacious`_.

    Returns
    -------
    callable
        A color filter function that has the form:

        def filter(input: np.ndarray[M, N, D])-> np.ndarray[M, N, D]

        where (M, N) are the image dimensions, and D is the color depth (3 for
        RGB, 4 for RGBA). Alpha is passed through unchanged and otherwise
        ignored.
    """
    if name not in _MENU_ENTRIES:
        raise ValueError(f"Unsupported filter name: {name!r}")
    name = _MENU_ENTRIES[name]

    if name is None:
        return None

    elif name == "greyscale":
        rgb_to_jch = colorspacious.cspace_converter("sRGB1", "JCh")
        jch_to_rgb = colorspacious.cspace_converter("JCh", "sRGB1")

        def convert(im):
            greyscale_JCh = rgb_to_jch(im)
            greyscale_JCh[..., 1] = 0
            im = jch_to_rgb(greyscale_JCh)
            return im

    else:
        cvd_space = {"name": "sRGB1+CVD", "cvd_type": name, "severity": 100}
        convert = colorspacious.cspace_converter(cvd_space, "sRGB1")

    def filter_func(im, dpi):
        alpha = None
        if im.shape[-1] == 4:
            im, alpha = im[..., :3], im[..., 3]
        im = convert(im)
        if alpha is not None:
            im = np.dstack((im, alpha))
        return np.clip(im, 0, 1), 0, 0

    return filter_func
```

### Step 3: Set menu entry

We define a function that sets the menu entry based on the selected color filter name. This function updates the color filter function based on the selection.

```python
def _set_menu_entry(tb, name):
    tb.canvas.figure.set_agg_filter(_get_color_filter(name))
    tb.canvas.draw_idle()
```

### Step 4: Set up the toolbar

Next, we define a function that sets up the toolbar based on the type of backend used. This function creates a button that allows the user to select the type of color filter to simulate.

```python
def setup(figure):
    tb = figure.canvas.toolbar
    if tb is None:
        return
    for cls in type(tb).__mro__:
        pkg = cls.__module__.split(".")[0]
        if pkg != "matplotlib":
            break
    if pkg == "gi":
        _setup_gtk(tb)
    elif pkg in ("PyQt5", "PySide2", "PyQt6", "PySide6"):
        _setup_qt(tb)
    elif pkg == "tkinter":
        _setup_tk(tb)
    elif pkg == "wx":
        _setup_wx(tb)
    else:
        raise NotImplementedError("The current backend is not supported")
```

### Step 5: Create sample images

We create sample images to demonstrate the color filter function. We import a sample image of Grace Hopper and plot it using Matplotlib. We also create a plot of sinusoidal waves.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    from matplotlib import cbook

    plt.rcParams['figure.hooks'].append('mplcvd:setup')

    fig, axd = plt.subplot_mosaic(
        [
            ['viridis', 'turbo'],
            ['photo', 'lines']
        ]
    )

    delta = 0.025
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    Z = (Z1 - Z2) * 2

    imv = axd['viridis'].imshow(
        Z, interpolation='bilinear',
        origin='lower', extent=[-3, 3, -3, 3],
        vmax=abs(Z).max(), vmin=-abs(Z).max()
    )
    fig.colorbar(imv)
    imt = axd['turbo'].imshow(
        Z, interpolation='bilinear', cmap='turbo',
        origin='lower', extent=[-3, 3, -3, 3],
        vmax=abs(Z).max(), vmin=-abs(Z).max()
    )
    fig.colorbar(imt)

    # A sample image
    with cbook.get_sample_data('grace_hopper.jpg') as image_file:
        photo = plt.imread(image_file)
    axd['photo'].imshow(photo)

    th = np.linspace(0, 2*np.pi, 1024)
    for j in [1, 2, 4, 6]:
        axd['lines'].plot(th, np.sin(th * j), label=f'$\\omega={j}$')
    axd['lines'].legend(ncols=2, loc='upper right')
    plt.show()
```

## Summary

In this lab, we learned how to simulate color vision deficiencies using Matplotlib. We used the colorspacious module to convert the input image to a different color space based on the selected color filter name. We also created sample images to demonstrate the color filter function.
