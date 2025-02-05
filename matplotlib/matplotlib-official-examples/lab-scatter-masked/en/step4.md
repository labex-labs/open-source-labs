# Adding a Line to Demarcate Masked Regions

Finally, we add a line to demarcate the masked regions. We create an array of theta values and plot a circle with radius `r0` using `np.cos(theta)` and `np.sin(theta)`.

```python
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
```
