# Crear una figura con subfiguras

Para crear una figura con subfiguras, primero debes crear un objeto figura usando `plt.figure()`. Luego, puedes crear subfiguras usando `fig.subfigures()`.

```python
fig = plt.figure()
subfigs = fig.subfigures(2, 1)
```

Esto creará una figura con dos subfiguras, una encima de la otra.
