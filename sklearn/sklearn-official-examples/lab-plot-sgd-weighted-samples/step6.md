# Add Legend and Display the Plot

We add a legend to the plot to differentiate between the unweighted and weighted models. We then display the plot.

```python
no_weights_handles, _ = no_weights.legend_elements()
weights_handles, _ = samples_weights.legend_elements()
ax.legend(
    [no_weights_handles[0], weights_handles[0]],
    ["no weights", "with weights"],
    loc="lower left",
)

ax.set(xticks=(), yticks=())
plt.show()
```
