# Create Subplots for Example Plots

We will create a 3 x 3 grid of subplots to display our example plots.

```python
fig, axs = plt.subplots(
    3, 3, figsize=(9, 9), layout="constrained", gridspec_kw={"hspace": 0.1})
```
