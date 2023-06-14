# Add Legend

We will add a legend to the plot using the `legend` function from `matplotlib.pyplot`. We will set the labels to `"non weighted"` and `"weighted"`, respectively.

```python
plt.legend(
    [disp.surface_.collections[0], wdisp.surface_.collections[0]],
    ["non weighted", "weighted"],
    loc="upper right",
)
```


