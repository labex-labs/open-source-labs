# Create a Log-Log Plot with Adjustable Datalim

Next, we will create a log-log plot with an adjustable datalim. This means that both the x-axis and y-axis will have logarithmic scales, and the aspect ratio of the plot will be adjusted to fit the data.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-")
ax.set_xlim(1e-1, 1e2)
ax.set_ylim(1e-1, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Datalim")
plt.show()
```
