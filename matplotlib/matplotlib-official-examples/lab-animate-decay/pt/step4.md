# Definir a função de inicialização

Precisamos definir uma função de inicialização que definirá o estado inicial do gráfico. Nesta função, definiremos os limites do eixo y e limparmos os dados do objeto de linha.

```python
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,
```
