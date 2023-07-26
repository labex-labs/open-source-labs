# Create the Subplots

Next, we will create two subplots - one for the outliers and one for the majority of the data. We will use `plt.subplots` to create the subplots and set the `sharex` parameter to `True` so that they share the same x-axis.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
```
