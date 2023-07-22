# Python Matplotlib Tutorial: Creating a Percentiles Horizontal Bar Chart

## Introduction

In this lab, we will learn how to create a horizontal bar chart using Python's Matplotlib library. We will use the example of gym teachers wanting to show parents how their child did across a handful of fitness tests, relative to other children. We will make up some data for little Johnny Doe to extract the plotting code for demo purposes.

## Steps

### Step 1: Import Libraries

We begin by importing the necessary libraries. We will use `numpy` to create our data, and `matplotlib.pyplot` to plot our graph.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define the Data

We define our data using named tuples. We define a `Student` tuple with the student's name, grade, and gender. We also define a `Score` tuple with the score value, unit, and percentile.

```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['value', 'unit', 'percentile'])
```

### Step 3: Define Helper Functions

We define two helper functions. The first function, `to_ordinal`, converts an integer to an ordinal string (e.g. 2 -> '2nd'). The second function, `format_score`, creates score labels for the right y-axis as the test name followed by the measurement unit (if any), split over two lines.

```python
def to_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    return v + suffixes[v[-1]]

def format_score(score):
    return f'{score.value}\n{score.unit}' if score.unit else str(score.value)
```

### Step 4: Define the Plotting Function

We define a function called `plot_student_results` that takes in a `Student` tuple, a dictionary of scores by test, and the cohort size. This function creates a horizontal bar chart of the percentile rankings for each test, relative to the student's grade and gender cohort.

```python
def plot_student_results(student, scores_by_test, cohort_size):
    fig, ax1 = plt.subplots(figsize=(9, 7), layout='constrained')
    fig.canvas.manager.set_window_title('Fitness Chart')

    ax1.set_title(student.name)
    ax1.set_xlabel(
        'Percentile Ranking Across {grade} Grade {gender}s\n'
        'Cohort Size: {cohort_size}'.format(
            grade=to_ordinal(student.grade),
            gender=student.gender.title(),
            cohort_size=cohort_size))

    test_names = list(scores_by_test.keys())
    percentiles = [score.percentile for score in scores_by_test.values()]

    rects = ax1.barh(test_names, percentiles, align='center', height=0.5)

    large_percentiles = [to_ordinal(p) if p > 40 else '' for p in percentiles]
    small_percentiles = [to_ordinal(p) if p <= 40 else '' for p in percentiles]
    ax1.bar_label(rects, small_percentiles,
                  padding=5, color='black', fontweight='bold')
    ax1.bar_label(rects, large_percentiles,
                  padding=-32, color='white', fontweight='bold')

    ax1.set_xlim([0, 100])
    ax1.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    ax1.xaxis.grid(True, linestyle='--', which='major',
                   color='grey', alpha=.25)
    ax1.axvline(50, color='grey', alpha=0.25)

    ax2 = ax1.twinx()
    ax2.set_ylim(ax1.get_ylim())
    ax2.set_yticks(
        np.arange(len(scores_by_test)),
        labels=[format_score(score) for score in scores_by_test.values()])

    ax2.set_ylabel('Test Scores')
```

### Step 5: Define the Data for the Plot

We define the data for the plot using the named tuples we defined earlier. We create a `Student` tuple for Johnny Doe, and a dictionary of `Score` tuples for each test.

```python
student = Student(name='Johnny Doe', grade=2, gender='Boy')
scores_by_test = {
    'Pacer Test': Score(7, 'laps', percentile=37),
    'Flexed Arm\n Hang': Score(48, 'sec', percentile=95),
    'Mile Run': Score('12:52', 'min:sec', percentile=73),
    'Agility': Score(17, 'sec', percentile=60),
    'Push Ups': Score(14, '', percentile=16),
}
```

### Step 6: Plot the Data

We call the `plot_student_results` function with the student data, scores by test, and cohort size as arguments, and then we call `plt.show()` to display the plot.

```python
plot_student_results(student, scores_by_test, cohort_size=62)
plt.show()
```

## Summary

In this lab, we learned how to create a horizontal bar chart using Python's Matplotlib library. We used an example of gym teachers wanting to show parents how their child did across a handful of fitness tests, relative to other children. We defined our data using named tuples, and we defined helper functions to convert integers to ordinal strings and to create score labels for the right y-axis. We defined a plotting function that creates a horizontal bar chart of the percentile rankings for each test, relative to the student's grade and gender cohort. We then called the plotting function with our data and displayed the plot.
