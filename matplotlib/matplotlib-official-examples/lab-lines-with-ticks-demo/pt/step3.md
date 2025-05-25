# Plotar uma Linha Curva com Ticked Patheffect

Agora, plotaremos uma linha curva com o efeito de caminho (patheffect) de marcas (ticked).

```python
# Plot a curved line with ticked style path
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```
