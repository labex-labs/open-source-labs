# Criar o gráfico

O próximo passo é criar o gráfico. Isso pode ser feito usando a função `ContourSet`.

```python
fig, ax = plt.subplots()

# Contornos preenchidos usando filled=True.
cs = ContourSet(ax, [0, 1, 2], [filled01, filled12], filled=True, cmap=cm.bone)
cbar = fig.colorbar(cs)

# Linhas de contorno (não preenchidas).
lines = ContourSet(
    ax, [0, 1, 2], [lines0, lines1, lines2], cmap=cm.cool, linewidths=3)
cbar.add_lines(lines)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 4.5),
       title='User-specified contours')
```
