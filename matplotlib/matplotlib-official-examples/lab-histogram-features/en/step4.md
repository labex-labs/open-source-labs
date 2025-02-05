# Add a best fit line

In this step, we will add a best fit line to the histogram. We will calculate the y-values for the line and plot it on top of the histogram.

```python
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
```
