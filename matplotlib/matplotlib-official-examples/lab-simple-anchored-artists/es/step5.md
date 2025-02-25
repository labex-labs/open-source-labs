# Agregar una barra de escala

Dibuja una barra horizontal con una longitud de 0.1 en coordenadas de datos, con una etiqueta fija debajo.

```python
asb = AnchoredSizeBar(ax.transData,
                      0.1,
                      r"1$^{\prime}$",
                      loc='lower center',
                      pad=0.1, borderpad=0.5, sep=5,
                      frameon=False)
ax.add_artist(asb)
```
