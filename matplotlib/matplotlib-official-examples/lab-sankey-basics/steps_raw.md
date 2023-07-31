# Python Matplotlib Tutorial - Creating Sankey Diagrams

## Introduction

Sankey diagrams are flow diagrams that show the movement of resources or energy between different stages or systems. In this tutorial, we will use the Matplotlib library in Python to create Sankey diagrams.

## Steps

### Step 1: Import necessary libraries

Before we start creating Sankey diagrams, we need to import the necessary libraries. In this tutorial, we will be using the Matplotlib library.

```python
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
```

### Step 2: Create a simple Sankey diagram

We will start by creating a simple Sankey diagram that demonstrates how to use the Sankey class.

```python
Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("The default settings produce a diagram like this.")
```

This code will produce a Sankey diagram with default settings, which includes the labels and orientations of the flows. The resulting diagram will be displayed with the title "The default settings produce a diagram like this."

### Step 3: Customize the Sankey diagram

We can customize the Sankey diagram by changing the flows, labels, orientations, and other parameters. In this example, we will create a diagram with longer paths and a label in the middle.

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Flow Diagram of a Widget")
sankey = Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=180,
                format='%.0f', unit='%')
sankey.add(flows=[25, 0, 60, -10, -20, -5, -15, -10, -40],
           labels=['', '', '', 'First', 'Second', 'Third', 'Fourth',
                   'Fifth', 'Hurray!'],
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0],
           pathlengths=[0.25, 0.25, 0.25, 0.25, 0.25, 0.6, 0.25, 0.25,
                        0.25],
           patchlabel="Widget\nA")  # Arguments to matplotlib.patches.PathPatch
diagrams = sankey.finish()
diagrams[0].texts[-1].set_color('r')
diagrams[0].text.set_fontweight('bold')
```

This code will create a Sankey diagram with longer paths, a label in the middle, and other customized parameters. The resulting diagram will be displayed with the title "Flow Diagram of a Widget."

### Step 4: Connect two systems in a Sankey diagram

We can also connect two systems in a Sankey diagram. In this example, we will create a diagram with two systems that are connected.

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Two Systems")
flows = [0.25, 0.15, 0.60, -0.10, -0.05, -0.25, -0.15, -0.10, -0.35]
sankey = Sankey(ax=ax, unit=None)
sankey.add(flows=flows, label='one',
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0])
sankey.add(flows=[-0.25, 0.15, 0.1], label='two',
           orientations=[-1, -1, -1], prior=0, connect=(0, 0))
diagrams = sankey.finish()
diagrams[-1].patch.set_hatch('/')
plt.legend()
```

This code will create a Sankey diagram with two systems that are connected. The resulting diagram will be displayed with the title "Two Systems."

## Summary

In this tutorial, we learned how to create Sankey diagrams using the Matplotlib library in Python. We started with a simple diagram and then customized it by changing the flows, labels, orientations, and other parameters. We also learned how to connect two systems in a Sankey diagram. With these tools, we can create informative and visually appealing flow diagrams for a variety of applications.
