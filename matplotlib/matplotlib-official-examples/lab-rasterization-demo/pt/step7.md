# Criar um gráfico pcolormesh com texto sobreposto com rasterização

Criaremos um gráfico pcolormesh com texto sobreposto com rasterização para ilustrar como a rasterização pode permitir que gráficos vetoriais mantenham as vantagens dos gráficos vetoriais para alguns artistas, como os eixos e o texto.

```python
ax4.set_aspect(1)
m = ax4.pcolormesh(xx, yy, d, zorder=-10)
ax4.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax4.transAxes)
ax4.set_rasterization_zorder(0)
ax4.set_title("Rasterization z$<-10$")
```
