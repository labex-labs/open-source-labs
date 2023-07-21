# Matplotlib Tutorial Lab

## Introduction

In this lab, you will learn how to use Python's Matplotlib library to create plots and graphs. Matplotlib is a powerful library that allows you to create a wide range of visualizations, from simple line plots to complex heatmaps. By the end of this lab, you will have a good understanding of how to use Matplotlib to create basic visualizations.

## Steps

### Step 1: Install Matplotlib

Before we can start using Matplotlib, we need to install it. You can install Matplotlib using pip, which is a package manager for Python. Open your terminal or command prompt and type the following command:

```
pip install matplotlib
```

### Step 2: Import Matplotlib

Once you have installed Matplotlib, you can import it in your Python code. To import Matplotlib, add the following line to the top of your Python script:

```python
import matplotlib.pyplot as plt
```

### Step 3: Create a Simple Line Plot

Let's start by creating a simple line plot. In this example, we will plot the sine and cosine functions over the interval [0, 2π].

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```

### Step 4: Customize the Plot

You can customize the plot by changing the colors, line styles, and markers. Here's an example:

```python
plt.plot(x, y1, 'r--', label='sin')
plt.plot(x, y2, 'g:', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```

### Step 5: Create a Scatter Plot

In addition to line plots, Matplotlib can also create scatter plots. Here's an example:

```python
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 500 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.show()
```

### Step 6: Create a Bar Plot

Matplotlib can also create bar plots. Here's an example:

```python
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Plot')
plt.show()
```

## Summary

In this lab, you learned how to use Matplotlib to create basic visualizations, including line plots, scatter plots, and bar plots. You also learned how to customize the plots by changing colors, line styles, and markers. Matplotlib is a powerful library that allows you to create a wide range of visualizations, and with practice, you can create even more complex visualizations.
