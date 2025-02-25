# Dibujar la línea de conexión

El quinto paso es dibujar una línea discontinua que conecte las dos subtramas. Creamos un objeto `ConnectionPatch` que conecta el origen de la subtrama izquierda con el borde derecho de la subtrama derecha. También guardamos el objeto de parche `con`, que actualizaremos más adelante en la animación.

```python
con = ConnectionPatch(
    (1, 0),
    (0, 0),
    "data",
    "data",
    axesA=axl,
    axesB=axr,
    color="C0",
    ls="dotted",
)
fig.add_artist(con)
```
