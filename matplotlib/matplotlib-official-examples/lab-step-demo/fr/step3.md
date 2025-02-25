# Tracer à l'aide de `.step()`

Nous pouvons utiliser la fonction `.step()` pour créer des courbes à valeur constante par morceaux. Le paramètre `where` détermine où les étapes doivent être dessinées. Nous allons créer trois tracés en utilisant différentes valeurs pour `where`.

```python
plt.step(x, y + 2, label='pre (default)', where='pre')
plt.step(x, y + 1, label='mid', where='mid')
plt.step(x, y, label='post', where='post')
plt.legend()
plt.show()
```

Le code ci-dessus créera un tracé avec trois courbes à valeur constante par morceaux, chacune avec une valeur différente pour `where`.
