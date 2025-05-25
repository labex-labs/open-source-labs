# Criar a animação

Usaremos um loop `for` para iterar por cada quadro da animação. Em cada iteração, limparemos o eixo, plotaremos o quadro atual, definiremos o título e faremos uma pausa por um curto período de tempo para permitir que a animação seja exibida.

```python
fig, ax = plt.subplots()

for i, img in enumerate(data):
    ax.clear()
    ax.imshow(img)
    ax.set_title(f"frame {i}")
    plt.pause(0.1)
```
