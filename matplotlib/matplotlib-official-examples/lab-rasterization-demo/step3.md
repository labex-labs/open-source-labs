# Create a figure with four subplots

We will create a figure with four subplots to illustrate the different aspects of rasterization.

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```
