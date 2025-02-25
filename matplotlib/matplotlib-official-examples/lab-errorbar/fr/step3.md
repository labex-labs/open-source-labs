# Tracez le graphique

Maintenant que nous avons nos données d'exemple, nous pouvons tracer le graphique en utilisant la fonction `errorbar()`. Nous passerons les tableaux `x` et `y` comme les deux premiers paramètres. Nous spécifierons ensuite l'erreur dans la direction x comme étant 0,2 et l'erreur dans la direction y comme étant 0,4 en utilisant respectivement les paramètres `xerr` et `yerr`.

```python
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()
```
