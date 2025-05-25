# Criar a Animação

O sétimo passo é criar o objeto de animação usando a função `FuncAnimation`. Passamos o objeto da figura, a função de animação, o intervalo entre os quadros em milissegundos, o número de quadros e um atraso antes de repetir a animação.

```python
ani = animation.FuncAnimation(
    fig,
    animate,
    interval=50,
    blit=False,  # blitting can't be used with Figure artists
    frames=x,
    repeat_delay=100,
)
```
