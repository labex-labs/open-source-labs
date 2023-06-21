# Create the figure and subplots

In this step, we will create a figure with two subplots for the cumulative distributions. We will also set the figure size to 9x4.

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```

#
