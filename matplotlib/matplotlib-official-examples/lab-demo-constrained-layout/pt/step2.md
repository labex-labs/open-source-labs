# Definindo um Gráfico de Exemplo

Definimos uma função que cria um gráfico de linha simples com rótulos x e y e um título.

```python
def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=12)
    ax.set_ylabel('y-label', fontsize=12)
    ax.set_title('Title', fontsize=14)
```
