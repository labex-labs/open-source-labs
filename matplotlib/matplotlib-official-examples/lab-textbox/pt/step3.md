# Definir a Função Submit

Definimos a função `submit` que será chamada quando o usuário enviar a entrada de texto. Esta função atualiza a função plotada com base na entrada do usuário.

```python
def submit(expression):
    """
    Atualiza a função plotada para a nova *expressão* matemática.

    *expression* é uma string usando "t" como sua variável independente, por exemplo,
    "t ** 3".
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
```
