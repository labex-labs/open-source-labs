# Ajustez un estimateur de densité à noyau

Maintenant, nous allons créer une instance de l'estimateur `KernelDensity` et l'ajuster à nos données. Nous pouvons choisir le type de noyau et la largeur de bande pour l'estimateur. Par exemple, nous pouvons utiliser un noyau gaussien et définir la largeur de bande sur 0,2.

```python
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
```
