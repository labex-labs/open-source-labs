# Matplotlib Text Object Concatenation

## Introduction

In this lab, you will learn how to concatenate text objects with different properties using Matplotlib. Concatenation is the process of combining multiple text objects into a single string. This can be useful when creating annotations or labels for visualizations.

## Steps

### Step 1: Create the First Text Object

The first step is to create the first text object using `~.Axes.text`. This text object will be the starting point for the concatenation process. The following code creates a red text object with the word "Matplotlib" at position (0.1, 0.5) on the plot.

```python
text = ax.text(.1, .5, "Matplotlib", color="red")
```

### Step 2: Create the Subsequent Text Objects

The next step is to create the subsequent text objects using `~.Axes.annotate`. This function allows you to position the text object relative to the previous text object. The following code creates three text objects that are positioned to the right of the previous text object.

```python
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # custom properties
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # custom properties
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # custom properties
```

### Step 3: Customize the Text Objects

You can customize the appearance of the text objects using various properties. In the previous code block, we set the color, weight, style, and family properties for each text object. You can experiment with different properties to achieve the desired appearance.

### Step 4: Display the Plot

Once you have created and customized all the text objects, you can display the plot using `plt.show()`. The following code block shows the complete code for the plot.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 20
ax = plt.figure().add_subplot(xticks=[], yticks=[])

# The first word, created with text().
text = ax.text(.1, .5, "Matplotlib", color="red")
# Subsequent words, positioned with annotate(), relative to the preceding one.
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # custom properties
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # custom properties
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # custom properties

plt.show()
```

## Summary

In this lab, you learned how to concatenate text objects with different properties using Matplotlib. You can use this technique to create custom annotations or labels for your visualizations. By customizing the appearance of each text object, you can create visually appealing and informative plots.
