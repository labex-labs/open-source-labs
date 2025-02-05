# Creating Notched Box Plot

We will now create a notched box plot with the `boxplot()` function. We will set the `notch` parameter to `True` to create a notched box plot.

```python
fig, ax2 = plt.subplots(figsize=(9, 4))
bplot2 = ax2.boxplot(all_data,
                     notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # x-tick labels
ax2.set_title('Notched Box Plot')
```
