# Create a Log-Log Plot with Adjustable Box

Next, we will create a log-log plot with an adjustable box. This means that both the x-axis and y-axis will have logarithmic scales, and the aspect ratio of the plot will be equal to 1.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e1, 1e3)
ax.set_ylim(1e2, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Box")
plt.show()
```
