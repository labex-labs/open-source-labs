# Create two histograms with stacked bars

We can create two histograms with stacked bars by calling the `hist` function twice and setting the `histtype` parameter to `'barstacked'`. In this example, we will create two histograms with stacked bars.

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```
