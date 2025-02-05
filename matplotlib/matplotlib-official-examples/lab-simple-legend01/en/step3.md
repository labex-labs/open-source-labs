# Add a legend to the plot

We will now add a legend to the plot. There are two ways to add a legend in Matplotlib. We will use both methods in this example.

```python
# Method 1: Place a legend above the subplot
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncols=2, mode="expand", borderaxespad=0.)

# Method 2: Place a legend to the right of the subplot
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
```
