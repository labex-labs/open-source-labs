# Matplotlib Tutorial: Controlling Style of Text and Labels Using a Dictionary

## Introduction

In this lab, we will learn how to control the style of text and labels in a Matplotlib plot using a dictionary. By creating a dictionary of options, we can share parameters across multiple text objects and labels. This will allow us to easily customize the font family, color, weight, and size of text in our plots.

## Steps

### Step 1: Import the Necessary Libraries

We will start by importing the necessary libraries for this tutorial. We will be using Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the Font Dictionary

Next, we will define the font dictionary that will contain the style options for our text and labels. In this example, we will set the font family to 'serif', the color to 'darkred', the weight to 'normal', and the size to 16.

```python
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
```

### Step 3: Create the Plot

Now, we can create our plot. We will generate some data using NumPy and plot a damped exponential decay curve.

```python
x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

plt.plot(x, y, 'k')
```

### Step 4: Customize the Title

We can customize the title of our plot using the font dictionary that we defined earlier. We will set the fontdict parameter of the title() function to our font dictionary.

```python
plt.title('Damped Exponential Decay', fontdict=font)
```

### Step 5: Add Text to the Plot

We can add text to our plot using the text() function. In this example, we will add a LaTeX expression to the plot using the font dictionary to customize the style.

```python
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
```

### Step 6: Customize the Axis Labels

We can customize the axis labels of our plot using the font dictionary as well. We will set the fontdict parameter of the xlabel() and ylabel() functions to our font dictionary.

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```

### Step 7: Adjust the Spacing

Finally, we can adjust the spacing of our plot to prevent the clipping of the ylabel. We will use the subplots_adjust() function to adjust the left margin.

```python
plt.subplots_adjust(left=0.15)
```

## Summary

In this lab, we learned how to control the style of text and labels in a Matplotlib plot using a dictionary. By creating a font dictionary, we can easily customize the font family, color, weight, and size of text in our plots. We used this technique to customize the title, text, and axis labels of our plot, and adjusted the spacing to prevent clipping of the ylabel.
