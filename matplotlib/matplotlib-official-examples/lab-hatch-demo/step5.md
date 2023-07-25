# Create a Plot with Hatched Patches

You can also use hatching with patches in your plot. In this case, we will be using the fill_between function to create a hatched patch.

```python
x = np.arange(0, 40, 0.2)
plt.fill_between(x, np.sin(x) * 4 + 30, y2=0, hatch='///', zorder=2, fc='c')
```
