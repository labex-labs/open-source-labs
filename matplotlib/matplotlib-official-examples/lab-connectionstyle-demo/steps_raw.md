# Python Matplotlib Tutorial - Annotation Connection Styles

## Introduction

This lab will guide you through the process of creating annotation connection styles using the Matplotlib library in Python. Annotations are an important tool in data visualization as they help to explain or highlight specific data points on a graph. The connection style of an annotation refers to the shape and style of the line connecting the annotation to the data point.

## Steps

### Step 1: Import the necessary libraries

Before we can create our annotations, we need to import the necessary libraries. In this case, we will be using the Matplotlib library.

```python
import matplotlib.pyplot as plt
```

### Step 2: Define the function for creating annotation connection styles

We will define a function that takes in two parameters: the axis object and the connection style. The function will plot two data points and create an annotation with the specified connection style.

```python
def demo_con_style(ax, connectionstyle):
    x1, y1 = 0.3, 0.2
    x2, y2 = 0.8, 0.6

    ax.plot([x1, x2], [y1, y2], ".")
    ax.annotate("",
                xy=(x1, y1), xycoords='data',
                xytext=(x2, y2), textcoords='data',
                arrowprops=dict(arrowstyle="->", color="0.5",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle=connectionstyle,
                                ),
                )

    ax.text(.05, .95, connectionstyle.replace(",", ",\n"),
            transform=ax.transAxes, ha="left", va="top")
```

### Step 3: Create the annotation connection styles

We will create various annotation connection styles using the `demo_con_style` function and plot them on a grid.

```python
fig, axs = plt.subplots(3, 5, figsize=(7, 6.3), layout="constrained")
demo_con_style(axs[0, 0], "angle3,angleA=90,angleB=0")
demo_con_style(axs[1, 0], "angle3,angleA=0,angleB=90")
demo_con_style(axs[0, 1], "arc3,rad=0.")
demo_con_style(axs[1, 1], "arc3,rad=0.3")
demo_con_style(axs[2, 1], "arc3,rad=-0.3")
demo_con_style(axs[0, 2], "angle,angleA=-90,angleB=180,rad=0")
demo_con_style(axs[1, 2], "angle,angleA=-90,angleB=180,rad=5")
demo_con_style(axs[2, 2], "angle,angleA=-90,angleB=10,rad=5")
demo_con_style(axs[0, 3], "arc,angleA=-90,angleB=0,armA=30,armB=30,rad=0")
demo_con_style(axs[1, 3], "arc,angleA=-90,angleB=0,armA=30,armB=30,rad=5")
demo_con_style(axs[2, 3], "arc,angleA=-90,angleB=0,armA=0,armB=40,rad=0")
demo_con_style(axs[0, 4], "bar,fraction=0.3")
demo_con_style(axs[1, 4], "bar,fraction=-0.3")
demo_con_style(axs[2, 4], "bar,angle=180,fraction=-0.2")

for ax in axs.flat:
    ax.set(xlim=(0, 1), ylim=(0, 1.25), xticks=[], yticks=[], aspect=1.25)
fig.set_constrained_layout_pads(wspace=0, hspace=0, w_pad=0, h_pad=0)

plt.show()
```

### Step 4: Interpret the results

The resulting grid of annotations with different connection styles will be displayed. The annotations help to highlight the data points on the graph and the different styles show the versatility of the annotation feature in Matplotlib.

## Summary

This lab provided an overview of how to create annotation connection styles using the Matplotlib library in Python. Annotations are a useful tool in data visualization and can be used to explain or highlight specific data points on a graph. The connection style of an annotation refers to the shape and style of the line connecting the annotation to the data point. By following the steps outlined in this lab, you should now be able to create your own annotation connection styles in Matplotlib.
