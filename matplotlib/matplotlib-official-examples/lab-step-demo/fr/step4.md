# Tracer à l'aide de `.plot()`

Nous pouvons obtenir le même comportement que `.step()` en utilisant le paramètre `drawstyle` de la fonction `.plot()`. Nous allons créer trois tracés en utilisant différentes valeurs pour `drawstyle`.

```python
plt.plot(x, y + 2, drawstyle='steps', label='steps (=steps-pre)')
plt.plot(x, y + 1, drawstyle='steps-mid', label='steps-mid')
plt.plot(x, y, drawstyle='steps-post', label='steps-post')
plt.legend()
plt.show()
```

Le code ci-dessus créera un tracé avec trois courbes à valeur constante par morceaux, chacune avec une valeur différente pour `drawstyle`.
