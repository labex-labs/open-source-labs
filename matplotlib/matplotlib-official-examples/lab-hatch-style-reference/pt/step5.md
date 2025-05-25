# Criar o segundo conjunto de padrões de hachura

Criaremos o segundo conjunto de padrões de hachura repetindo cada padrão duas vezes para aumentar a densidade. Usaremos a seguinte lista:

```python
hatches = ['//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**']
```

Usaremos o mesmo loop que antes para criar os retângulos.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
