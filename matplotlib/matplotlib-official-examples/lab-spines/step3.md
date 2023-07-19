# Create Subplots

We will create three subplots to demonstrate different spine customizations. We will use constrained layout to ensure that the labels do not overlap the axes.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, layout='constrained')
```
