# Criar Subplots

Em seguida, criamos os subplots usando `plt.subplot_mosaic`. Criaremos uma grade 3x2 de subplots e os rotularemos da seguinte forma:

- O gráfico superior esquerdo será rotulado como "a)"
- O gráfico inferior esquerdo será rotulado como "b)"
- Os gráficos superior direito e inferior direito serão rotulados como "c)" e "d)", respectivamente.

```python
fig, axs = plt.subplot_mosaic([['a)', 'c)'], ['b)', 'c)'], ['d)', 'd)']], layout='constrained')
```
