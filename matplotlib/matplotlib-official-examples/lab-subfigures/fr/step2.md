# Créer une figure avec des sous-figures

Pour créer une figure avec des sous-figures, vous devez tout d'abord créer un objet figure à l'aide de `plt.figure()`. Ensuite, vous pouvez créer des sous-figures à l'aide de `fig.subfigures()`.

```python
fig = plt.figure()
subfigs = fig.subfigures(2, 1)
```

Cela créera une figure avec deux sous-figures, l'une au-dessus de l'autre.
