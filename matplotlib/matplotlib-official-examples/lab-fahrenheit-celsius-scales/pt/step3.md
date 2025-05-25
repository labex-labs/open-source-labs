# Definir uma função para atualizar o segundo eixo

Definiremos uma função closure para registrar como um callback para atualizar o segundo eixo de acordo com o primeiro eixo.

```python
def convert_ax_c_to_celsius(ax_f):
    """
    Atualiza o segundo eixo de acordo com o primeiro eixo.
    """
    y1, y2 = ax_f.get_ylim()
    ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
    ax_c.figure.canvas.draw()
```
