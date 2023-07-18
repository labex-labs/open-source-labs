# Python Matplotlib Tutorial: Creating a Plot with Custom Fonts

## Introduction

In this lab, you will learn how to create a plot with custom fonts using the Python Matplotlib library. You will be introduced to the `pgf.texsystem` parameter that allows you to use LaTeX to customize the font family of your plot.

## Steps

### Step 1: Import Matplotlib and Set the pgf.texsystem Parameter

First, you need to import the Matplotlib library and set the `pgf.texsystem` parameter to `pdflatex`. This parameter allows you to use LaTeX to customize the font family of your plot.

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```

### Step 2: Define the Font Family

Next, you need to define the font family that you want to use in your plot. In this example, we will use the `cmbright` font family.

```python
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "pgf.preamble": "\n".join([
         r"\usepackage[utf8x]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage{cmbright}",
    ]),
})
```

### Step 3: Create the Plot

Now, you can create your plot using the `plt.subplots()` function. In this example, we will create a simple line plot.

```python
fig, ax = plt.subplots(figsize=(4.5, 2.5))

ax.plot(range(5))
```

### Step 4: Add Text to the Plot

You can add text to your plot using the `ax.text()` function. In this example, we will add text with different font families.

```python
ax.text(0.5, 3., "serif", family="serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="sans-serif")
ax.set_xlabel(r"µ is not $\mu$")
```

### Step 5: Adjust the Layout and Save the Plot

Finally, you can adjust the layout of your plot and save it to a file using the `fig.tight_layout()` and `fig.savefig()` functions, respectively.

```python
fig.tight_layout(pad=.5)

fig.savefig("pgf_texsystem.pdf")
fig.savefig("pgf_texsystem.png")
```

## Summary

In this lab, you learned how to create a plot with custom fonts using the Python Matplotlib library. You used the `pgf.texsystem` parameter to set the font family of your plot and the `ax.text()` function to add text with different font families. You also learned how to adjust the layout of your plot and save it to a file.
