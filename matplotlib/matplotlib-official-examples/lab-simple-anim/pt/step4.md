# Definir a Função de Animação

A função de animação será chamada pela função `FuncAnimation()` e será usada para atualizar o gráfico com novos dados. Neste exemplo, atualizaremos os valores do eixo y do gráfico de linha com uma onda senoidal que tem uma amplitude variável ao longo do tempo.

```python
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,
```
