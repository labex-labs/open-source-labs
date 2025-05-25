# Visualizar a estimativa de densidade

Finalmente, podemos visualizar a estimativa de densidade usando um histograma e a função de densidade estimada. Podemos plotar o histograma dos dados originais, bem como a função de densidade estimada.

```python
import matplotlib.pyplot as plt

bins = np.linspace(-5, 5, 50)
plt.hist(X, bins=bins, density=True, alpha=0.5, label='Histograma')
plt.plot(X, np.exp(scores), color='red', label='Estimativa de Densidade Kernel')
plt.legend()
plt.show()
```
