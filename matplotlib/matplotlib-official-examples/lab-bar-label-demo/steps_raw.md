# Python Matplotlib Tutorial

## Bar Chart Labeling

### Introduction

In this tutorial, we will learn how to use the `bar_label` helper function in Matplotlib to create labeled bar charts. We will cover various scenarios such as labeling horizontal and vertical bar charts, using different label formats, and customizing label appearance.

### Steps

#### Step 1: Import Libraries

First, we need to import the necessary libraries, including `numpy` and `matplotlib`. We will also use the `random` module from `numpy` to generate some random data.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)
```

#### Step 2: Vertical Bar Chart Labeling

We will start by creating a vertical bar chart and labeling it using the `bar_label` function. The data we will use is the number of penguins by sex, taken from https://allisonhorst.github.io/palmerpenguins/.

```python
species = ('Adelie', 'Chinstrap', 'Gentoo')
sex_counts = {
    'Male': np.array([73, 34, 61]),
    'Female': np.array([73, 34, 58]),
}
width = 0.6  # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()
bottom = np.zeros(3)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()
```

#### Step 3: Horizontal Bar Chart Labeling

Next, we will create a horizontal bar chart and label it using the `bar_label` function. We will use the data from the previous step, but this time we will generate some random performance data for each person.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Label with specially formatted floats
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)  # adjust xlim to fit labels

plt.show()
```

#### Step 4: Advanced Bar Labeling

In this step, we will show some more advanced things that can be done with bar labels. We will use the same horizontal bar chart as in the previous step.

```python
fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Label with given captions, custom padding and annotate options
ax.bar_label(hbars, labels=[f'±{e:.2f}' for e in error],
             padding=8, color='b', fontsize=14)
ax.set_xlim(right=16)

plt.show()
```

#### Step 5: Bar Labeling Using `{}`-Style Format String

In this step, we will show how to use a `{}`-style format string to format bar labels. We will use some data on gelato sales by flavor.

```python
fruit_names = ['Coffee', 'Salted Caramel', 'Pistachio']
fruit_counts = [4000, 2000, 7000]

fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor', ylim=(0, 8000))
ax.bar_label(bar_container, fmt='{:,.0f}')
```

#### Step 6: Bar Labeling Using a Callable

Finally, we will show how to use a callable to format bar labels. We will use some data on running speeds of different animals.

```python
animal_names = ['Lion', 'Gazelle', 'Cheetah']
mph_speed = [50, 60, 75]

fig, ax = plt.subplots()
bar_container = ax.bar(animal_names, mph_speed)
ax.set(ylabel='speed in MPH', title='Running speeds', ylim=(0, 80))
ax.bar_label(bar_container, fmt=lambda x: f'{x * 1.61:.1f} km/h')
```

### Summary

In this tutorial, we learned how to use the `bar_label` helper function in Matplotlib to create labeled bar charts. We covered various scenarios such as labeling horizontal and vertical bar charts, using different label formats, and customizing label appearance.
