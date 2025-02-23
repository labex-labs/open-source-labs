# Créer des données et un histogramme

Créez des données et un histogramme à l'aide de NumPy.

```python
# histogram our data with numpy
data = np.random.randn(1000)
n, _, _ = plt.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
```
