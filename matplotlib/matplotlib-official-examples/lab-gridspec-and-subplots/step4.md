# Remove the Underlying Axes

We remove the underlying axes that are covered by the bigger axes that we will create in the next step.

```python
for ax in axs[1:, -1]:
    ax.remove()
```
