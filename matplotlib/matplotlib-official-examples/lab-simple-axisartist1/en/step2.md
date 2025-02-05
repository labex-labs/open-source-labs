# Create Figure and Subplots

We will create a figure with two subplots using the `add_gridspec` method.

```python
fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)
```
