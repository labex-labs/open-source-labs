# Visualisez l'estimation de la densité

Enfin, nous pouvons visualiser l'estimation de la densité en utilisant un histogramme et la fonction de densité estimée. Nous pouvons tracer l'histogramme des données d'origine ainsi que la fonction de densité estimée.

```python
import matplotlib.pyplot as plt

bins = np.linspace(-5, 5, 50)
plt.hist(X, bins=bins, density=True, alpha=0.5, label='Histogramme')
plt.plot(X, np.exp(scores), color='red', label='Estimation de la densité à noyau')
plt.legend()
plt.show()
```
