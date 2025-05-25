# Definir a Função Adicionar Eixo Flutuante

Defina a função `add_floating_axis`, que adiciona um eixo flutuante ao gráfico. Esta função recebe o objeto `ax1` como argumento e retorna o objeto `axis`.

```python
def add_floating_axis(ax1):
    # Define the floating axis
    ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)

    return axis
```
