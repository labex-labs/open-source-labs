# Adicionando Eixos Flutuantes

Definiremos duas funções que adicionarão eixos flutuantes ao nosso gráfico. A primeira função `add_floating_axis1()` adiciona um eixo flutuante ao gráfico com o rótulo `theta = 30`. A segunda função `add_floating_axis2()` adiciona um eixo flutuante ao gráfico com o rótulo `r = 6`.

```python
def add_floating_axis1(ax):
    ax.axis["lat"] = axis = ax.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)
    return axis

def add_floating_axis2(ax):
    ax.axis["lon"] = axis = ax.new_floating_axis(1, 6)
    axis.label.set_text(r"$r = 6$")
    axis.label.set_visible(True)
    return axis
```
