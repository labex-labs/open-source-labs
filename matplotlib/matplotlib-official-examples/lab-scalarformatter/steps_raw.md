# Python Matplotlib Tutorial Lab

## Introduction

This tutorial lab will guide you through the process of formatting tick labels using the Python Matplotlib library. It will cover the default tick formatter and various configurations possible via `~.axes.Axes.ticklabel_format`.

## Steps

### Step 1: Import Required Libraries

In order to use the Python Matplotlib library, we need to import it into our Python environment. Additionally, we will be using the NumPy library to generate data for our example plots.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Data for Example Plots

We will generate data for three plots to demonstrate the different configurations possible with `~.axes.Axes.ticklabel_format`.

```python
x = np.arange(0, 1, .01)

# Plot 1
plot1_x = x * 1e5 + 1e10
plot1_y = x * 1e-10 + 1e-5

# Plot 2
plot2_x = x * 1e5
plot2_y = x * 1e-4

# Plot 3
plot3_x = -x * 1e5 - 1e10
plot3_y = -x * 1e-5 - 1e-10
```

### Step 3: Create Subplots for Example Plots

We will create a 3 x 3 grid of subplots to display our example plots.

```python
fig, axs = plt.subplots(
    3, 3, figsize=(9, 9), layout="constrained", gridspec_kw={"hspace": 0.1})
```

### Step 4: Plot Data on Subplots

We will plot our generated data on the subplots we created in Step 3.

```python
for col in axs.T:
    col[0].plot(plot1_x, plot1_y)
    col[1].plot(plot2_x, plot2_y)
    col[2].plot(plot3_x, plot3_y)
```

### Step 5: Configure Tick Label Formatting

We will configure the tick label formatting for our subplots. The first subplot will use the default settings, the second subplot will use fancy formatting of mathematical expressions, and the third subplot will not use offset notation.

```python
# Subplot 1 (default settings)
axs[0, 0].set_title("default settings")

# Subplot 2 (useMathText=True)
for ax in axs[:, 1]:
    ax.ticklabel_format(useMathText=True)
axs[0, 1].set_title("useMathText=True")

# Subplot 3 (useOffset=False)
for ax in axs[:, 2]:
    ax.ticklabel_format(useOffset=False)
axs[0, 2].set_title("useOffset=False")
```

### Step 6: Display Example Plots

We will display the example plots with the configured tick label formatting.

```python
plt.rcParams.update({"axes.titleweight": "bold", "axes.titley": 1.1})
plt.show()
```

## Summary

In this tutorial lab, we learned how to format tick labels using the Python Matplotlib library. We generated data for three example plots and configured the tick label formatting for each plot. We displayed the example plots to visualize the different tick label formatting configurations.
