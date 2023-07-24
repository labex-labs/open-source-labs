# Plotting with Categorical Variables

Matplotlib allows you to create plots using categorical variables. Let's create a bar plot, scatter plot, and line plot with categorical variables:

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()
```

Explanation:

- We create a list `names` with three categorical values and a list `values` representing their corresponding values.
- The `figure` function is called to create a new figure with a specified size.
- We use the `subplot` function to create a grid of subplots. In this example, we create three subplots, each with a different type of plot: bar plot, scatter plot, and line plot.
- The `suptitle` function is used to set the super-title of the figure.
