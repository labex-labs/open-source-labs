# Configurar o retângulo

Definiremos a posição e as dimensões do retângulo usando as variáveis `left`, `bottom`, `width` e `height`. Em seguida, criaremos o retângulo usando a classe `Rectangle` e o adicionaremos ao gráfico usando o método `add_patch`.

```python
left, bottom, width, height = (-1, -1, 2, 2)
rect = plt.Rectangle((left, bottom), width, height,
                     facecolor="black", alpha=0.1)

fig, ax = plt.subplots()
ax.add_patch(rect)
```
