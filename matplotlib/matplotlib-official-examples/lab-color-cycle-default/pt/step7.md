# Personalizar os ticks do eixo y

Personalizamos os ticks do eixo y para os subplots mais à esquerda.

```python
for irow in range(2):
    axs[irow, 0].yaxis.set_ticks(np.arange(0, 10, 2))
```
