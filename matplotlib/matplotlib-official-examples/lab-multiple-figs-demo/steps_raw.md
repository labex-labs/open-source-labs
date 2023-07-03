# Python Matplotlib Lab

## Managing Multiple Figures in Pyplot

### Introduction

In this lab, you will learn how to manage multiple figures in Matplotlib's pyplot. Matplotlib is a popular data visualization library in Python, and pyplot is a sub-library within Matplotlib that provides a simple interface for creating, customizing, and organizing plots. You will learn how to create and switch between multiple figures, create subplots within each figure, and make changes to specific subplots.

### Steps

#### Step 1: Import necessary libraries

The first step is to import the necessary libraries. In this case, we need `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

#### Step 2: Create data

Next, we need to create some data to plot. We will create two sine waves that we will plot in separate figures.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)
```

#### Step 3: Create figure 1

We will begin by creating the first figure, which will contain two subplots. We will plot the first sine wave in the top subplot and twice the amplitude of the first sine wave in the bottom subplot.

```python
plt.figure(1)

# Top subplot
plt.subplot(211)
plt.plot(t, s1)

# Bottom subplot
plt.subplot(212)
plt.plot(t, 2*s1)
```

#### Step 4: Create figure 2

Next, we will create a second figure that will contain a single plot of the second sine wave.

```python
plt.figure(2)
plt.plot(t, s2)
```

#### Step 5: Make changes to figure 1

Now, we will switch back to the first figure and make some changes. We will plot the second sine wave in the top subplot using square markers, and remove the x-axis tick labels from the top subplot.

```python
plt.figure(1)

# Top subplot
plt.subplot(211)
plt.plot(t, s2, 's')
ax = plt.gca()
ax.set_xticklabels([])
```

#### Step 6: Display the figures

Finally, we will display the figures using the `plt.show()` function.

```python
plt.show()
```

### Summary

In this lab, you learned how to manage multiple figures in Matplotlib's pyplot. You learned how to create figures and subplots, switch between figures, and make changes to specific subplots. With this knowledge, you can create more complex plots with multiple figures and subplots, and customize each plot to your liking.
