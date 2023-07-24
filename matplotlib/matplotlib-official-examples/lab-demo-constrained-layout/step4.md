# Creating Subplots With Constrained Layout

We create the same 2x2 subplots, but this time we use _constrained layout_. This automatically adjusts the subplots to prevent overlaps between axes objects and labels.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')

for ax in axs.flat:
    example_plot(ax)
```
