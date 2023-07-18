# Python Matplotlib Lab

## Introduction

In this lab, we will learn how to wrap text automatically in Python Matplotlib. We will also explore how to control the placement and style of text in a Matplotlib plot.

## Steps

### Step 1: Setting up the Environment

Before we begin, we need to ensure that Matplotlib is installed. Open your terminal and type the following command:

```python
!pip install matplotlib
```

### Step 2: Creating a Basic Plot

Let's start by creating a basic plot with a text element. In your Python script, add the following code:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, "Hello, Matplotlib!", ha='center')
plt.show()
```

### Step 3: Wrapping Text Automatically

Now, let's explore how to wrap text automatically in Matplotlib. Replace the `plt.text()` line in your code with the following:

```python
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(5, 5, t, ha='center', wrap=True)
```

The `wrap=True` argument tells Matplotlib to wrap the text automatically.

### Step 4: Controlling Text Placement and Style

We can also control the placement and style of the text in our Matplotlib plot. Try adding the following code to your script:

```python
plt.text(2, 8, "Top Left", fontsize=12, color='red')
plt.text(8, 8, "Top Right", fontsize=12, color='blue')
plt.text(2, 2, "Bottom Left", fontsize=12, color='green')
plt.text(8, 2, "Bottom Right", fontsize=12, color='purple')
```

This will add four text elements to our plot, each with a different color, font size, and position.

### Step 5: Saving the Plot

Finally, let's save our plot as an image file. Add the following code to your script:

```python
fig.savefig("my_plot.png")
```

This will save our plot as a PNG image in the same directory as our script.

## Summary

In this lab, we learned how to wrap text automatically in Python Matplotlib. We also explored how to control the placement and style of text in a Matplotlib plot. With these tools, we can create clear and visually appealing plots for our data.
