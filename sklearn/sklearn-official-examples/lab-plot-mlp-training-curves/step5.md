# Plot the learning curves for each dataset

Finally, we can plot the learning curves for each dataset using the plot_on_dataset function. We will create a 2x2 plot and plot each dataset on a separate axis.

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

for ax, data, name in zip(
    axes.ravel(), data_sets, ["iris", "digits", "circles", "moons"]
):
    plot_on_dataset(*data, ax=ax, name=name)

fig.legend(ax.get_lines(), labels, ncol=3, loc="upper center")
plt.show()
```
