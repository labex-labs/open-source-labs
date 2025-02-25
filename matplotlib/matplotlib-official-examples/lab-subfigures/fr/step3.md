# Tracer des données sur les sous-figures

Pour tracer des données sur les sous-figures, vous devez créer un sous-graphique pour chaque sous-figure à l'aide de `subfig.subplots()`. Ensuite, vous pouvez utiliser l'une des fonctions de tracé de Matplotlib pour créer les tracés.

```python
ax1 = subfigs[0].subplots()
ax1.plot(np.arange(10), np.random.randn(10))

ax2 = subfigs[1].subplots()
ax2.plot(np.arange(10), np.random.randn(10))
```

Cela créera deux sous-figures, chacune avec un tracé de données aléatoires.
