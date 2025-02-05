# Create subplots

We will create a 2x3 grid of subplots using `subplots()` function.

```python
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained")
```
