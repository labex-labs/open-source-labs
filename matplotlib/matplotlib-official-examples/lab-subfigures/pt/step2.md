# Criar uma Figura com Subfiguras

Para criar uma figura com subfiguras, você primeiro precisa criar um objeto figura usando `plt.figure()`. Em seguida, você pode criar subfiguras usando `fig.subfigures()`.

```python
fig = plt.figure()
subfigs = fig.subfigures(2, 1)
```

Isso criará uma figura com duas subfiguras, uma acima da outra.
