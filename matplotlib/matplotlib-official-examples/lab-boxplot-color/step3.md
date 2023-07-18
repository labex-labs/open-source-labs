# Creating Rectangular Box Plot

We will now create a rectangular box plot using the `boxplot()` function in Matplotlib. We will set the `patch_artist` parameter to `True` to fill the box with color.

```python
fig, ax1 = plt.subplots(figsize=(9, 4))
bplot1 = ax1.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # x-tick labels
ax1.set_title('Rectangular Box Plot')
```
