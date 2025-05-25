# Adicionar Efeito de Contorno ao Texto

Podemos adicionar um efeito de contorno (stroke effect) ao texto usando o efeito de caminho `withStroke`. Neste exemplo, adicionaremos um efeito de contorno à anotação de texto no gráfico.

```python
# Create plot and add text annotation with stroke effect
fig, ax = plt.subplots()
ax.imshow(arr)
txt = ax.annotate("test", (1., 1.), (0., 0),
                   arrowprops=dict(arrowstyle="->",
                                   connectionstyle="angle3", lw=2),
                   size=20, ha="center",
                   path_effects=[patheffects.withStroke(linewidth=3,
                                                        foreground="w")])
txt.arrow_patch.set_path_effects([
    patheffects.Stroke(linewidth=5, foreground="w"),
    patheffects.Normal()])

# Add grid with stroke effect
pe = [patheffects.withStroke(linewidth=3,
                             foreground="w")]
ax.grid(True, linestyle="-", path_effects=pe)

plt.show()
```
