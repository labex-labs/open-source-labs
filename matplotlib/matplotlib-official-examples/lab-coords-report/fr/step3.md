# Création du graphique

Maintenant que nous avons nos données, nous pouvons créer notre graphique à l'aide de Matplotlib. Dans cet exemple, nous allons créer un graphique de dispersion à l'aide de la fonction plot().

```python
fig, ax = plt.subplots()
plt.plot(x, y, 'o')
```
