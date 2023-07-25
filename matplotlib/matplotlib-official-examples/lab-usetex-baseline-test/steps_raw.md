# Matplotlib Tutorial: Text Baselines Comparison

## Introduction

In this lab, we will compare the text baselines computed for mathtext and usetex using Matplotlib library. We will create a plot that contains two subplots, one with mathtext and the other with usetex. Each subplot will display four test strings with different styles and positions.

## Steps

### Step 1: Import the necessary libraries

We need to import the `matplotlib.pyplot` library to create the plot.

```python
import matplotlib.pyplot as plt
```

### Step 2: Set the Matplotlib font

We need to set the font to be used for Matplotlib text. We will use the Computer Modern font and set it as the default font for Matplotlib.

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```

### Step 3: Create the subplots

We will create a figure that contains two subplots, one with mathtext and the other with usetex. We will use the `subplots()` method to create the subplots.

```python
fig, axs = plt.subplots(1, 2, figsize=(2 * 3, 6.5))
```

### Step 4: Add test strings to the plot

We will add four test strings to each subplot, each with a different style and position. We will use the `text()` method to add the text to the subplots.

```python
test_strings = ["lg", r"$\frac{1}{2}\pi$", r"$p^{3^A}$", r"$p_{3_2}$"]
for ax, usetex in zip(axs, [False, True]):
    ax.axvline(0, color="r")
    for i, s in enumerate(test_strings):
        ax.axhline(i, color="r")
        ax.text(0., 3 - i, s,
                usetex=usetex,
                verticalalignment="baseline",
                size=50,
                bbox=dict(pad=0, ec="k", fc="none"))
```

### Step 5: Set the plot limits and labels

We will set the plot limits and labels to match the desired output.

```python
for ax in axs:
    ax.set(xlim=(-0.1, 1.1), ylim=(-.8, 3.9), xticks=[], yticks=[])
    ax.set_title(f"usetex={ax.usetex}\n")
```

### Step 6: Display the plot

We will display the plot using the `show()` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to compare the text baselines computed for mathtext and usetex using Matplotlib. We created a plot that contained two subplots, one with mathtext and the other with usetex. We added four test strings to each subplot, each with a different style and position. Finally, we displayed the plot to compare the text baselines.
