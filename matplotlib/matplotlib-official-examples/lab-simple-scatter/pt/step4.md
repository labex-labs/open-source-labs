# Criando a Animação

A etapa final é criar a animação. Fazemos isso usando a função `FuncAnimation` do módulo `animation`. Esta função recebe alguns argumentos, incluindo o objeto `figure`, a função que atualizará o gráfico e o número de frames a serem usados.

```python
def animate(i):
    scat.set_offsets((x[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=50)
```
