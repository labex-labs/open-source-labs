# Criar um gráfico pcolormesh sem rasterização

Criaremos um gráfico pcolormesh sem rasterização para ilustrar a diferença entre rasterização e não rasterização.

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```
