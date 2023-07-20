# Ishikawa Diagram Creation Lab

## Introduction

In this lab, we will learn how to create an Ishikawa diagram, also known as a fishbone diagram or cause-and-effect diagram. Ishikawa diagrams are commonly used to identify problems in a system by showing how causes and effects are linked. We will use Python and the Matplotlib library to create the diagram.

## Steps

### Step 1: Install Matplotlib

Before we begin, we need to make sure we have Matplotlib installed. If you haven't already, you can install it using the following command:

```python
!pip install matplotlib
```

### Step 2: Import Libraries

We will begin by importing the necessary libraries. We will be using Matplotlib and the Polygon and Wedge classes from the matplotlib.patches module.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Wedge
```

### Step 3: Create the Fishbone Diagram

Now we will create the fishbone diagram. We will start by creating a figure and axis object.

```python
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
```

Next, we will set the x and y limits for the axis and turn off the axis.

```python
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
```

### Step 4: Define the Functions

We will define three functions that we will use to create the diagram.

#### Problems Function

The first function is the problems function. This function takes in the category name, the x and y positions of the problem arrow, and the angle of the problem annotation. It uses the annotate method to create the problem arrow and annotation.

```python
def problems(data: str,
             problem_x: float, problem_y: float,
             prob_angle_x: float, prob_angle_y: float):
    ax.annotate(str.upper(data), xy=(problem_x, problem_y),
                xytext=(prob_angle_x, prob_angle_y),
                fontsize='10',
                color='white',
                weight='bold',
                xycoords='data',
                verticalalignment='center',
                horizontalalignment='center',
                textcoords='offset fontsize',
                arrowprops=dict(arrowstyle="->", facecolor='black'),
                bbox=dict(boxstyle='square',
                          facecolor='tab:blue',
                          pad=0.8))
```

#### Causes Function

The second function is the causes function. This function takes in the list of causes, the x and y positions of the cause annotation, and whether the cause should be placed above or below the problem arrow. It uses the annotate method to create the cause annotation and arrow.

```python
def causes(data: list, cause_x: float, cause_y: float,
           cause_xytext=(-9, -0.3), top: bool = True):
    for index, cause in enumerate(data):
        coords = [[0, [0, 0]],
                  [0.23, [0.5, -0.5]],
                  [-0.46, [-1, 1]],
                  [0.69, [1.5, -1.5]],
                  [-0.92, [-2, 2]],
                  [1.15, [2.5, -2.5]]]
        if top:
            cause_y += coords[index][1][0]
        else:
            cause_y += coords[index][1][1]
        cause_x -= coords[index][0]
        ax.annotate(cause, xy=(cause_x, cause_y),
                    horizontalalignment='center',
                    xytext=cause_xytext,
                    fontsize='9',
                    xycoords='data',
                    textcoords='offset fontsize',
                    arrowprops=dict(arrowstyle="->",
                                    facecolor='black'))
```

#### Draw Body Function

The third function is the draw body function. This function takes in the input data and uses it to create the fishbone diagram.

```python
def draw_body(data: dict):
    second_sections = []
    third_sections = []
    if len(data) == 1 or len(data) == 2:
        spine_length = (-2.1, 2)
        head_pos = (2, 0)
        tail_pos = ((-2.8, 0.8), (-2.8, -0.8), (-2.0, -0.01))
        first_section = [1.6, 0.8]
    elif len(data) == 3 or len(data) == 4:
        spine_length = (-3.1, 3)
        head_pos = (3, 0)
        tail_pos = ((-3.8, 0.8), (-3.8, -0.8), (-3.0, -0.01))
        first_section = [2.6, 1.8]
        second_sections = [-0.4, -1.2]
    else:  # len(data) == 5 or 6
        spine_length = (-4.1, 4)
        head_pos = (4, 0)
        tail_pos = ((-4.8, 0.8), (-4.8, -0.8), (-4.0, -0.01))
        first_section = [3.5, 2.7]
        second_sections = [1, 0.2]
        third_sections = [-1.5, -2.3]

    for index, problem in enumerate(data.values()):
        top_row = True
        cause_arrow_y = 1.7
        if index % 2 != 0:
            top_row = False
            y_prob_angle = -16
            cause_arrow_y = -1.7
        else:
            y_prob_angle = 16
        if index in (0, 1):
            prob_arrow_x = first_section[0]
            cause_arrow_x = first_section[1]
        elif index in (2, 3):
            prob_arrow_x = second_sections[0]
            cause_arrow_x = second_sections[1]
        else:
            prob_arrow_x = third_sections[0]
            cause_arrow_x = third_sections[1]
        if index > 5:
            raise ValueError(f'Maximum number of problems is 6, you have entered '
                             f'{len(data)}')
        ax.plot(spine_length, [0, 0], color='tab:blue', linewidth=2)
        ax.text(head_pos[0] + 0.1, head_pos[1] - 0.05, 'PROBLEM', fontsize=10,
                weight='bold', color='white')
        semicircle = Wedge(head_pos, 1, 270, 90, fc='tab:blue')
        ax.add_patch(semicircle)
        triangle = Polygon(tail_pos, fc='tab:blue')
        ax.add_patch(triangle)
        problems(list(data.keys())[index], prob_arrow_x, 0, -12, y_prob_angle)
        causes(problem, cause_arrow_x, cause_arrow_y, top=top_row)
```

### Step 5: Input Data

Now we will define the input data. The data should be a dictionary where the keys are the categories and the values are lists of causes.

```python
categories = {
    'Method': ['Time consumption', 'Cost', 'Procedures', 'Inefficient process', 'Sampling'],
    'Machine': ['Faulty equipment', 'Compatibility'],
    'Material': ['Poor-quality input', 'Raw materials', 'Supplier', 'Shortage'],
    'Measurement': ['Calibration', 'Performance', 'Wrong measurements'],
    'Environment': ['Bad conditions'],
    'People': ['Lack of training', 'Managers', 'Labor shortage', 'Procedures', 'Sales strategy']
}
```

### Step 6: Draw the Fishbone Diagram

Finally, we will call the draw body function and show the diagram.

```python
draw_body(categories)
plt.show()
```

## Summary

In this lab, we learned how to create an Ishikawa diagram using Python and the Matplotlib library. We defined three functions to create the diagram and used a dictionary to define the input data. The resulting diagram shows how causes and effects are linked in a system and can be used to identify problems.
