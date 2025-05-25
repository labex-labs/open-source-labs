# Plotar a Superfície

```python
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
```

Plotamos a superfície usando a função `plot_surface()`. Passamos os valores `X`, `Y` e `Z`, bem como o parâmetro `cmap` definido como `cm.coolwarm` para colorir a superfície com o mapa de cores coolwarm. Também definimos `linewidth=0` para remover o wireframe (estrutura de arame) e `antialiased=False` para tornar a superfície opaca.
