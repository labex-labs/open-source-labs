# Add vertical lines to the histogram

To make it easier to see the effect of the thresholding, we will add vertical lines to the histogram to indicate the current threshold values. We will create two lines for the lower and upper threshold values, respectively.

```python
lower_limit_line = axs[1].axvline(slider.val[0], color='k')
upper_limit_line = axs[1].axvline(slider.val[1], color='k')
```
