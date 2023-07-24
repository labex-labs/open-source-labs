# Text Rotation Lab

## Introduction

This lab will demonstrate how to rotate text objects in Matplotlib relative to a line or object on a plot rather than the screen coordinate system. This technique can be helpful when you want to rotate text in relation to something specific on the plot.

## Steps

### Step 1: Plot a diagonal line

First, we will plot a diagonal line at a 45-degree angle using Matplotlib's `plot()` function.

```python
fig, ax = plt.subplots()

# Plot diagonal line (45 degrees)
h = ax.plot(range(0, 10), range(0, 10))
```

### Step 2: Adjust the limits of the plot

Next, we will adjust the limits of the plot so that the diagonal line is no longer at a 45-degree angle when viewed on the screen. This will create a scenario where we need to rotate text relative to the line, rather than the screen coordinate system.

```python
# set limits so that it no longer looks on screen to be 45 degrees
ax.set_xlim([-10, 20])
```

### Step 3: Define text locations and rotation angle

We will now define the locations where we want to plot text on the figure and the angle of rotation we want to use.

```python
# Locations to plot text
l1 = np.array((1, 1))
l2 = np.array((5, 5))

# Rotate angle
angle = 45
```

### Step 4: Plot text without correct rotation

We will now plot text at the specified locations without taking the rotation of the line into account. This will result in the text being rotated at a 45-degree angle, which is not what we want.

```python
# Plot text
th1 = ax.text(*l1, 'text not rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor')
```

### Step 5: Plot text with correct rotation

Finally, we will plot text at the specified locations while taking the rotation of the line into account. This will result in the text being rotated at the correct angle relative to the line.

```python
# Plot text
th2 = ax.text(*l2, 'text rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor',
              transform_rotates_text=True)
```

### Step 6: Display the figure

We will display the figure to see the difference between the two sets of plotted text.

```python
plt.show()
```

## Summary

In this lab, we learned how to rotate text objects in Matplotlib relative to a line or object on a plot. By using the `transform_rotates_text` parameter, we were able to ensure that the text was rotated at the correct angle in relation to the line, rather than the screen coordinate system.
