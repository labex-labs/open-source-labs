# Créez un histogramme avec des largeurs de bar personnalisées

Nous pouvons créer un histogramme avec des largeurs de bar personnalisées et inégales en fournissant une liste de limites de bar. Dans cet exemple, nous allons créer un histogramme avec des bar espacées de manière inégale.

```python
bins = [100, 150, 180, 195, 205, 220, 250, 300]
plt.hist(x, bins=bins, density=True, histtype='bar', rwidth=0.8)
plt.show()
```
