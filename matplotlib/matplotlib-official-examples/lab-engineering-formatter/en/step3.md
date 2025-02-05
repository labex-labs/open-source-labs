# Create the Figure and Subplots

We need to create a figure and subplots to display the data. In this lab, we will create two subplots, side by side.

```python
# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 9.6))
for ax in (ax0, ax1):
    ax.set_xscale('log')
```
