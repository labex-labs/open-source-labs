# Matplotlib Tutorial - Align y-labels

## Introduction

In this lab, you will learn how to align y-labels in Matplotlib plots. The alignment of y-labels is important for improving the readability of plots, especially when there are multiple subplots.

## Steps

### Step 1: Import Required Libraries

The first step is to import the required libraries. In this lab, we will be using Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create the Plot

The next step is to create the plot. We will create a plot with two subplots, where the y-labels are not aligned.

```python
def make_plot(axs):
    box = dict(facecolor='yellow', pad=5, alpha=0.2)

    # Fixing random state for reproducibility
    np.random.seed(19680801)
    ax1 = axs[0, 0]
    ax1.plot(2000*np.random.rand(10))
    ax1.set_title('ylabels not aligned')
    ax1.set_ylabel('misaligned 1', bbox=box)
    ax1.set_ylim(0, 2000)

    ax3 = axs[1, 0]
    ax3.set_ylabel('misaligned 2', bbox=box)
    ax3.plot(np.random.rand(10))

    ax2 = axs[0, 1]
    ax2.set_title('ylabels aligned')
    ax2.plot(2000*np.random.rand(10))
    ax2.set_ylabel('aligned 1', bbox=box)
    ax2.set_ylim(0, 2000)

    ax4 = axs[1, 1]
    ax4.plot(np.random.rand(10))
    ax4.set_ylabel('aligned 2', bbox=box)

fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)
plt.show()
```

### Step 3: Align Y-Labels Automatically

The third step is to align the y-labels automatically using the `.Figure.align_ylabels` method.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)
fig.align_ylabels(axs[:, 1])
plt.show()
```

### Step 4: Align Y-Labels Manually

The fourth step is to align the y-labels manually using the `~.Axis.set_label_coords` method of the y-axis object.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)

labelx = -0.3  # axes coords

for j in range(2):
    axs[j, 1].yaxis.set_label_coords(labelx, 0.5)

plt.show()
```

### Step 5: Summary

In this lab, you learned how to align y-labels in Matplotlib plots. The alignment of y-labels is important for improving the readability of plots, especially when there are multiple subplots. We covered two methods for aligning y-labels, one using a short call to `.Figure.align_ylabels` and the second a manual way to align the labels.

## Conclusion

Congratulations! You have learned how to align y-labels in Matplotlib plots. Keep practicing and exploring the Matplotlib library to improve your visualization skills.
