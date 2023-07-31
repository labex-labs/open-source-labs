# Creating Scatter Plots with Legends

## Introduction

Scatter plots are used to visualize the relationship between two variables. A scatter plot with a legend is useful when there are multiple groups in the data, and we want to distinguish between them in the plot. In this lab, we will learn how to create scatter plots with legends in Python using Matplotlib library.

## Steps

### Step 1: Importing Required Libraries

We begin by importing the necessary libraries, including NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Creating a Scatter Plot with Multiple Groups

We can create a scatter plot with multiple groups by looping through each group and creating a scatter plot for that group. We specify the color, size, and transparency of the markers for each group using the `c`, `s`, and `alpha` parameters, respectively. We also set the `label` parameter to the group name, which will be used in the legend.

```python
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
```

### Step 3: Automated Legend Creation

We can also use the `PathCollection.legend_elements` method to automatically create a legend for a scatter plot. This method will try to determine a useful number of legend entries to be shown and return a tuple of handles and labels.

```python
N = 45
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 220, size=N)

fig, ax = plt.subplots()

scatter = ax.scatter(x, y, c=c, s=s)

# produce a legend with the unique colors from the scatter
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Classes")
ax.add_artist(legend1)

# produce a legend with a cross-section of sizes from the scatter
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")

plt.show()
```

### Step 4: Customizing Legend Elements

We can further customize the legend elements by using additional arguments in the `PathCollection.legend_elements` method. For example, we can specify the number of legend entries to be created and how they should be labeled.

```python
volume = np.random.rayleigh(27, size=40)
amount = np.random.poisson(10, size=40)
ranking = np.random.normal(size=40)
price = np.random.uniform(1, 10, size=40)

fig, ax = plt.subplots()

# Because the price is much too small when being provided as size for ``s``,
# we normalize it to some useful point sizes, s=0.3*(price*3)**2
scatter = ax.scatter(volume, amount, c=ranking, s=0.3*(price*3)**2,
                     vmin=-3, vmax=3, cmap="Spectral")

# Produce a legend for the ranking (colors). Even though there are 40 different
# rankings, we only want to show 5 of them in the legend.
legend1 = ax.legend(*scatter.legend_elements(num=5),
                    loc="upper left", title="Ranking")
ax.add_artist(legend1)

# Produce a legend for the price (sizes). Because we want to show the prices
# in dollars, we use the *func* argument to supply the inverse of the function
# used to calculate the sizes from above. The *fmt* ensures to show the price
# in dollars. Note how we target at 5 elements here, but obtain only 4 in the
# created legend due to the automatic round prices that are chosen for us.
kw = dict(prop="sizes", num=5, color=scatter.cmap(0.7), fmt="$ {x:.2f}",
          func=lambda s: np.sqrt(s/.3)/3)
legend2 = ax.legend(*scatter.legend_elements(**kw),
                    loc="lower right", title="Price")

plt.show()
```

## Summary

In this lab, we learned how to create scatter plots with legends in Python using Matplotlib library. We created scatter plots with multiple groups and automated legend creation. We also customized the legend elements using the `PathCollection.legend_elements` method. Scatter plots with legends are useful for visualizing the relationship between two variables with multiple groups.
