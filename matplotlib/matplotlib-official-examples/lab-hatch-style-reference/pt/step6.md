# Criar o terceiro conjunto de padrões de hachura

Criaremos o terceiro conjunto de padrões de hachura combinando dois padrões para criar um novo. Usaremos a seguinte lista:

```python
hatches = ['/o', '\\|', '|*', '-\\', '+o', 'x*', 'o-', 'O|', 'O.', '*-']
```

Usaremos o mesmo loop que antes para criar os retângulos.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
