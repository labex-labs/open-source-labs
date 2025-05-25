# Criar o Objeto de Animação

Agora podemos criar o objeto de animação usando a função `FuncAnimation()`. Passaremos o objeto da figura, a função de animação, o intervalo de atualização e o número de frames a serem salvos.

```python
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
```
