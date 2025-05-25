# Criar a função `hatches_plot`

A função `hatches_plot` criará um retângulo com o padrão de hachura especificado e o adicionará ao eixo. Ela também adicionará um texto com o padrão de hachura.

```python
def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')
```
