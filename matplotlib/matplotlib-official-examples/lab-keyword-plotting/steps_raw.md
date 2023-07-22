# Plotting with Keywords

## Introduction

In this lab, you will learn how to generate plots using strings corresponding to variables using the `numpy.recarray` or `pandas.DataFrame` data format with the `data` keyword argument in Matplotlib.

## Steps

### Step 1: Import Required Libraries

In this step, we will import the necessary libraries to generate plots using keywords.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Set Seed Value

In this step, we will set the seed value for the random number generator to ensure that the results are reproducible.

```python
np.random.seed(19680801)
```

### Step 3: Create Data

In this step, we will create a dictionary `data` containing values for variables `a`, `b`, `c`, and `d`.

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
```

### Step 4: Generate Plot

In this step, we will generate a scatter plot using the `data` dictionary as input to the `scatter()` function. We will use the strings corresponding to the `a`, `b`, `c`, and `d` variables to generate the plot.

```python
fig, ax = plt.subplots()
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='entry a', ylabel='entry b')
plt.show()
```

### Step 5: Interpret the Plot

In this step, we will interpret the scatter plot generated in Step 4. The plot shows the relationship between the `a` and `b` variables, with the `c` variable used to determine the color of each point and the `d` variable used to determine the size of each point. The x-axis represents `entry a` and the y-axis represents `entry b`.

## Summary

In this lab, you learned how to generate plots using strings corresponding to variables using the `numpy.recarray` or `pandas.DataFrame` data format with the `data` keyword argument in Matplotlib. You also learned how to interpret a scatter plot using the `a`, `b`, `c`, and `d` variables.
