# Plotar Elipse usando Aproximação Poligonal

Nesta etapa, plotaremos a elipse usando uma aproximação poligonal.

```python
ax = fig.add_subplot(212, aspect='equal')
ax.fill(x, y, alpha=0.2, facecolor='green', edgecolor='green', zorder=1)
e2 = patches.Arc((xcenter, ycenter), width, height,
                 angle=angle, linewidth=2, fill=False, zorder=2)

ax.add_patch(e2)
fig.savefig('arc_compare')

plt.show()
```
