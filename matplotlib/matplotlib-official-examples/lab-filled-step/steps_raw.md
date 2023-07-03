# Matplotlib Histogram Lab

## Introduction

In this lab, we will learn how to create hatch-filled histograms using Matplotlib. A histogram is a graphical representation of data that uses bars to show the frequency of numerical data. A hatch-filled histogram is a histogram in which the bars are filled with a pattern of lines, dots, or other symbols.

## Steps

### Step 1: Import necessary libraries

We will import the necessary libraries for this lab. We need the following libraries:

- `numpy` for generating random data
- `matplotlib.pyplot` for creating plots
- `matplotlib.ticker` for setting axis tick locations
- `cycler` for creating style cycles
- `functools.partial` for creating a partial function

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from cycler import cycler
from functools import partial
```

### Step 2: Define the histogram function

We will define a function to draw a histogram as a stepped patch. The function will take the following parameters:

- `ax`: the Axes to plot to
- `edges`: a length n+1 array giving the left edges of each bin and the right edge of the last bin
- `values`: a length n array of bin counts or values
- `bottoms`: a float or array, optional, a length n array of the bottom of the bars. If None, zero is used.
- `orientation`: a string, optional, the orientation of the histogram. 'v' (default) has the bars increasing in the positive y-direction.

```python
def filled_hist(ax, edges, values, bottoms=None, orientation='v', **kwargs):
    """
    Draw a histogram as a stepped patch.

    Parameters
    ----------
    ax : Axes
        The axes to plot to

    edges : array
        A length n+1 array giving the left edges of each bin and the
        right edge of the last bin.

    values : array
        A length n array of bin counts or values

    bottoms : float or array, optional
        A length n array of the bottom of the bars.  If None, zero is used.

    orientation : {'v', 'h'}
       Orientation of the histogram.  'v' (default) has
       the bars increasing in the positive y-direction.

    **kwargs
        Extra keyword arguments are passed through to `.fill_between`.

    Returns
    -------
    ret : PolyCollection
        Artist added to the Axes
    """
    if orientation not in 'hv':
        raise ValueError(f"orientation must be in {{'h', 'v'}} not {orientation}")

    kwargs.setdefault('step', 'post')
    kwargs.setdefault('alpha', 0.7)
    edges = np.asarray(edges)
    values = np.asarray(values)
    if len(edges) - 1 != len(values):
        raise ValueError(f'Must provide one more bin edge than value not: {len(edges)=} {len(values)=}')

    if bottoms is None:
        bottoms = 0
    bottoms = np.broadcast_to(bottoms, values.shape)

    values = np.append(values, values[-1])
    bottoms = np.append(bottoms, bottoms[-1])
    if orientation == 'h':
        return ax.fill_betweenx(edges, values, bottoms, **kwargs)
    elif orientation == 'v':
        return ax.fill_between(edges, values, bottoms, **kwargs)
    else:
        raise AssertionError("you should never be here")
```

### Step 3: Define the stacked histogram function

We will define a function to create a stacked histogram. The function will take the following parameters:

- `ax`: the axes to add artists to
- `stacked_data`: a (M, N) shaped array. The first dimension will be iterated over to compute histograms row-wise
- `sty_cycle`: a Cycler or operable of dict, style to apply to each set
- `bottoms`: an array, default: 0, the initial positions of the bottoms.
- `hist_func`: a callable, optional. Must have signature `bin_vals, bin_edges = f(data)`. `bin_edges` expected to be one longer than `bin_vals`
- `labels`: a list of strings, optional, the label for each set. If not given and stacked data is an array defaults to 'default set {n}'. If stacked_data is a mapping and labels is None, default to the keys. If stacked_data is a mapping and labels is given then only the columns listed will be plotted.
- `plot_func`: a callable, optional, function to call to draw the histogram. Must have signature `ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **kwargs)`
- `plot_kwargs`: a dictionary, optional, any extra keyword arguments to pass through to the plotting function. This will be the same for all calls to the plotting function and will override the values in `sty_cycle`.

```python
def stack_hist(ax, stacked_data, sty_cycle, bottoms=None, hist_func=None, labels=None, plot_func=None, plot_kwargs=None):
    """
    Parameters
    ----------
    ax : axes.Axes
        The axes to add artists too

    stacked_data : array or Mapping
        A (M, N) shaped array.  The first dimension will be iterated over to
        compute histograms row-wise

    sty_cycle : Cycler or operable of dict
        Style to apply to each set

    bottoms : array, default: 0
        The initial positions of the bottoms.

    hist_func : callable, optional
        Must have signature `bin_vals, bin_edges = f(data)`.
        `bin_edges` expected to be one longer than `bin_vals`

    labels : list of str, optional
        The label for each set.

        If not given and stacked data is an array defaults to 'default set {n}'

        If *stacked_data* is a mapping, and *labels* is None, default to the
        keys.

        If *stacked_data* is a mapping and *labels* is given then only the
        columns listed will be plotted.

    plot_func : callable, optional
        Function to call to draw the histogram must have signature:

          ret = plot_func(ax, edges, top, bottoms=bottoms,
                          label=label, **kwargs)

    plot_kwargs : dict, optional
        Any extra keyword arguments to pass through to the plotting function.
        This will be the same for all calls to the plotting function and will
        override the values in *sty_cycle*.

    Returns
    -------
    arts : dict
        Dictionary of artists keyed on their labels
    """
    # deal with default binning function
    if hist_func is None:
        hist_func = np.histogram

    # deal with default plotting function
    if plot_func is None:
        plot_func = filled_hist

    # deal with default
    if plot_kwargs is None:
        plot_kwargs = {}

    try:
        l_keys = stacked_data.keys()
        label_data = True
        if labels is None:
            labels = l_keys

    except AttributeError:
        label_data = False
        if labels is None:
            labels = itertools.repeat(None)

    if label_data:
        loop_iter = enumerate((stacked_data[lab], lab, s) for lab, s in zip(labels, sty_cycle))
    else:
        loop_iter = enumerate(zip(stacked_data, labels, sty_cycle))

    arts = {}
    for j, (data, label, sty) in loop_iter:
        if label is None:
            label = f'dflt set {j}'
        label = sty.pop('label', label)
        vals, edges = hist_func(data)
        if bottoms is None:
            bottoms = np.zeros_like(vals)
        top = bottoms + vals
        sty.update(plot_kwargs)
        ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **sty)
        bottoms = top
        arts[label] = ret
    ax.legend(fontsize=10)
    return arts
```

### Step 4: Set up histogram function to fixed bins

We will set up a histogram function with fixed bins using `numpy.histogram`. We will create 20 bins ranging from -3 to 3.

```python
edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)
```

### Step 5: Set up style cycles

We will set up style cycles for the histograms using `cycler`. We will create three style cycles: one for the facecolor, one for the label, and one for the hatch pattern.

```python
color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler(label=[f'set {n}' for n in range(4)])
hatch_cycle = cycler(hatch=['/', '*', '+', '|'])
```

### Step 6: Generate random data

We will generate random data using `numpy.random.randn`. We will generate 4 sets of data with 12250 points each.

```python
np.random.seed(19680801)
stack_data = np.random.randn(4, 12250)
```

### Step 7: Create the hatch-filled histogram

We will create a hatch-filled histogram using the `stack_hist` function we defined earlier. We will use the `stack_data`, `color_cycle`, and `hist_func` we defined earlier. We will also set `plot_kwargs` to include edgecolor and orientation.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('counts')
ax1.set_xlabel('x')
ax2.set_xlabel('counts')
ax2.set_ylabel('x')
```

### Step 8: Create the labeled hatch-filled histogram

We will create a labeled hatch-filled histogram using the `stack_hist` function we defined earlier. We will use the `dict_data`, `color_cycle`, and `hist_func` we defined earlier. We will also set `labels` to `['set 0', 'set 3']` to plot only the first and last set.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True, sharey=True)
dict_data = dict(zip((c['label'] for c in label_cycle), stack_data))
arts = stack_hist(ax1, dict_data, color_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, dict_data, color_cycle + hatch_cycle, hist_func=hist_func, labels=['set 0', 'set 3'])
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax1.set_xlabel('counts')
ax1.set_ylabel('x')
ax2.set_ylabel('x')
```

## Summary

In this lab, we learned how to create hatch-filled histograms using Matplotlib. We defined two functions: `filled_hist` to draw a histogram as a stepped patch, and `stack_hist` to create a stacked histogram. We also set up a histogram function with fixed bins using `numpy.histogram`, and defined three style cycles for the histograms using `cycler`. Finally, we generated random data and created two hatch-filled histograms using the `stack_hist` function.
