# Create a figure and subplots

In this step, we will create a figure and four subplots for each of the projections we will create. We will use the `plt.subplots()` method to create a figure and subplots.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': 'aitoff'})
```
