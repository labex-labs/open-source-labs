# Criar a Animação

Agora, criaremos a animação usando a função `FuncAnimation` do Matplotlib.

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```
