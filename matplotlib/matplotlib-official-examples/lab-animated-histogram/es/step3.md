# Crear datos y histograma

Crea datos y un histograma utilizando NumPy.

```python
# hacemos un histograma de nuestros datos con numpy
data = np.random.randn(1000)
n, _, _ = plt.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
```
