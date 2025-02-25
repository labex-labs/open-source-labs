# Personnaliser l'axe Z

```python
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
```

Nous personnalisons l'axe z en utilisant la fonction `set_zlim()` pour définir les limites de l'axe z de -1,01 à 1,01. Nous utilisons ensuite la fonction `set_major_locator()` pour définir le nombre d'échelles sur l'axe z à 10 en utilisant `LinearLocator(10)`. Enfin, nous utilisons la fonction `set_major_formatter()` pour formater les étiquettes des échelles de l'axe z à l'aide d'un `StrMethodFormatter`.
