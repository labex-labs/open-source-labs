# Definir a Função de Animação

O sexto passo é definir a função de animação. Esta função será chamada para cada quadro da animação e atualizará a posição do ponto no subplot da esquerda, a posição e os dados da curva senoidal no subplot da direita e a posição do patch de conexão.

```python
def animate(i):
    x = np.linspace(0, i, int(i * 25 / np.pi))
    sine.set_data(x, np.sin(x))
    x, y = np.cos(i), np.sin(i)
    point.set_data([x], [y])
    con.xy1 = x, y
    con.xy2 = i, y
    return point, sine, con
```
