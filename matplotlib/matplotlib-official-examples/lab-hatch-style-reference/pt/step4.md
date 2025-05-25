# Criar o primeiro conjunto de padrões de hachura

Criaremos o primeiro conjunto de padrões de hachura usando a seguinte lista:

```python
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
```

Em seguida, usaremos um loop para criar um retângulo com cada padrão de hachura e adicioná-lo a um subplot.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
