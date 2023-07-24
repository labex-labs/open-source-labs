# Matplotlib Quiver Plot Lab

## Introduction

This lab will guide you through how to create a quiver plot using Matplotlib in Python. A quiver plot displays vector fields as arrows. It is useful in visualizing fluid flows, electric and magnetic fields, and other types of vector fields.

## Steps

### Step 1: Import Libraries

We need to import the `numpy` and `matplotlib` libraries to create a quiver plot.

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Step 2: Create Data

We need to create the `X` and `Y` coordinates using the `np.meshgrid()` function. Then, we create the `U` and `V` arrays that represent the vector fields.

```python
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
```

### Step 3: Create the Quiver Plot

We can create the quiver plot using the `ax.quiver()` function. We pass in the `X`, `Y`, `U`, and `V` arrays as parameters.

```python
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
```

### Step 4: Create the Quiver Key

We can add a quiver key to the plot to show the scale of the arrows. We use the `ax.quiverkey()` function to add the key. We pass in the `q` object, the `X` and `Y` position of the key, the length of the arrow, the label for the key, and the position of the label.

```python
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')
```

### Step 5: Display the Plot

We can display the plot using the `plt.show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a quiver plot using Matplotlib in Python. We started by importing the necessary libraries, creating the data, and then creating the quiver plot. Finally, we added a quiver key to the plot and displayed it.
