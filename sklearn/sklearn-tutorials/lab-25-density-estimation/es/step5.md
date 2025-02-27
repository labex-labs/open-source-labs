# Visualizar la estimación de densidad

Finalmente, podemos visualizar la estimación de densidad usando un histograma y la función de densidad estimada. Podemos trazar el histograma de los datos originales así como la función de densidad estimada.

```python
import matplotlib.pyplot as plt

bins = np.linspace(-5, 5, 50)
plt.hist(X, bins=bins, density=True, alpha=0.5, label='Histogram')
plt.plot(X, np.exp(scores), color='red', label='Kernel Density Estimate')
plt.legend()
plt.show()
```
