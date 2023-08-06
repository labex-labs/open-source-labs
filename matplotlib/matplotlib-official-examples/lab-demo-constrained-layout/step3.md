# Creating Subplots Without Constrained Layout

We create a figure with 2x2 subplots without using _constrained layout_. This results in overlapping labels on the axes.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout=None)

for ax in axs.flat:
    example_plot(ax)
```
