# Definiendo un gráfico de ejemplo

Definimos una función que crea un gráfico de línea simple con etiquetas de eje x e y y un título.

```python
def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=12)
    ax.set_ylabel('y-label', fontsize=12)
    ax.set_title('Title', fontsize=14)
```
