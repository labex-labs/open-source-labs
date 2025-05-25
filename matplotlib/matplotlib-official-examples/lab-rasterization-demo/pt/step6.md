# Criar um gráfico pcolormesh com texto sobreposto sem rasterização

Criaremos um gráfico pcolormesh com texto sobreposto sem rasterização para ilustrar como gráficos vetoriais podem manter as vantagens dos gráficos vetoriais para alguns artistas, como os eixos e o texto.

```python
ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterization")
```
