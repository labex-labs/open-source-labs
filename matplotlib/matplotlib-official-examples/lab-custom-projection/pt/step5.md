# Criar Exemplo

Finalmente, criaremos um exemplo usando a projeção personalizada.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # Agora, faça um exemplo simples usando a projeção personalizada.
    fig, ax = plt.subplots(subplot_kw={'projection': 'custom_hammer'})
    ax.plot([-1, 1, 1], [-1, -1, 1], "o-")
    ax.grid()

    plt.show()
```
