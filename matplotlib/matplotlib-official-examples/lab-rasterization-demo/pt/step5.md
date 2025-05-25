# Criar um gráfico pcolormesh com rasterização

Criaremos um gráfico pcolormesh com rasterização para ilustrar como a rasterização pode acelerar a renderização e produzir arquivos menores.

```python
ax2.set_aspect(1)
ax2.set_title("Rasterization")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```
