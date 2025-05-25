# Definir a função de animação

Agora, precisamos definir a função que atualizará o gráfico para cada quadro da animação. Esta função receberá os dados gerados pela função `data_gen()` e atualizará o gráfico com os novos dados. Também atualizaremos os limites do eixo x à medida que a animação progride.

```python
def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,
```
