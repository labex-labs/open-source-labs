# Unicode Minus Lab

## Introduction

In this lab, we will learn how to control the tick labels in a Matplotlib plot using Unicode minus and ASCII hyphen. By default, tick labels at negative values are rendered using a Unicode minus rather than an ASCII hyphen. However, this can be controlled by setting `axes.unicode_minus`. We will use a sample code snippet to showcase the difference between the two glyphs in a magnified font.

## Steps

### Step 1: Importing the Required Libraries

We will start by importing the required libraries `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Setting up the Data

Next, we will create some sample data to plot using the `numpy` library. We will create a linearly spaced array of 100 values between 0 and 10.

```python
x = np.linspace(0, 10, 100)
```

### Step 3: Plotting the Data

Now, we will plot the data using the `plot` function of Matplotlib. We will plot a sine wave with a frequency of 1 and amplitude of 1.

```python
y = np.sin(x)
plt.plot(x, y)
```

### Step 4: Setting the Tick Labels

By default, tick labels at negative values are rendered using a Unicode minus rather than an ASCII hyphen. However, we can change this behavior by setting `axes.unicode_minus` to `False`.

```python
plt.rcParams['axes.unicode_minus'] = False
```

### Step 5: Displaying the Plot

Finally, we will display the plot using the `show` function of Matplotlib.

```python
plt.show()
```

## Summary

In this lab, we learned how to control the tick labels in a Matplotlib plot using Unicode minus and ASCII hyphen. We used a sample code snippet to showcase the difference between the two glyphs in a magnified font. By setting `axes.unicode_minus` to `False`, we can change the default behavior of rendering tick labels at negative values using a Unicode minus.
