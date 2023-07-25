# Matplotlib Eventplot Lab

## Introduction

In this lab, you will learn how to create an event plot using Matplotlib. An event plot is a way to show the occurrence of events over time. The events can be represented as lines or dots. This lab will guide you through creating horizontal and vertical event plots with different line properties.

## Steps

### Step 1: Import libraries and set random seed

We will start by importing the necessary libraries and setting a random seed for reproducibility.

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams['font.size'] = 8.0

# Fixing random state for reproducibility
np.random.seed(19680801)
```

### Step 2: Create random data

Next, we will create some random data to use for our event plots.

```python
data1 = np.random.random([6, 50])
```

### Step 3: Set colors and line properties for the first event plot

We will set different colors and line properties for each set of positions in the first event plot.

```python
colors1 = [f'C{i}' for i in range(6)]

lineoffsets1 = [-15, -3, 1, 1.5, 6, 10]
linelengths1 = [5, 2, 1, 1, 3, 1.5]
```

### Step 4: Create the first event plot - horizontal orientation

We will create the first event plot in a horizontal orientation.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)
```

### Step 5: Create the first event plot - vertical orientation

We will create the first event plot in a vertical orientation.

```python
axs[1, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1, orientation='vertical')
```

### Step 6: Create random data for the second event plot

We will create another set of random data for the second event plot. We will use the gamma distribution for aesthetic purposes.

```python
data2 = np.random.gamma(4, size=[60, 50])
```

### Step 7: Set line properties for the second event plot

We will use individual values for the line properties in the second event plot. These values will be used for all data sets except for lineoffsets2, which sets the increment between each data set.

```python
colors2 = 'black'
lineoffsets2 = 1
linelengths2 = 1
```

### Step 8: Create the second event plot - horizontal orientation

We will create the second event plot in a horizontal orientation.

```python
axs[0, 1].eventplot(data2, colors=colors2, lineoffsets=lineoffsets2,
                    linelengths=linelengths2)
```

### Step 9: Create the second event plot - vertical orientation

We will create the second event plot in a vertical orientation.

```python
axs[1, 1].eventplot(data2, colors=colors2, lineoffsets=lineoffsets2,
                    linelengths=linelengths2, orientation='vertical')
```

### Step 10: Show the event plots

We will show the event plots using `plt.show()`.

```python
plt.show()
```

## Summary

In this lab, you learned how to create event plots in Matplotlib. You learned how to create horizontal and vertical event plots with different line properties. By following the step-by-step guide, you can easily create your own event plots for your data.
