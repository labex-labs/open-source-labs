# Criando a figura e a imagem

Em seguida, criamos a figura e a imagem que queremos colocar nela. Neste exemplo, criamos um array 100x100 de valores aleatórios e definimos os valores na metade direita da imagem como 1. Em seguida, criamos duas instâncias separadas da imagem, cada uma com uma posição e opacidade diferentes.

```python
fig = plt.figure()
Z = np.arange(10000).reshape((100, 100))
Z[:, 50:] = 1

im1 = fig.figimage(Z, xo=50, yo=0, origin='lower')
im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')
```
