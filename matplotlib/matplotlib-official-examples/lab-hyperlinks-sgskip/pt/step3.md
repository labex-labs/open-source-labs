# Criar uma Imagem com um Hiperlink

Nesta etapa, criaremos uma imagem e adicionaremos um hiperlink a ela. Aqui está o código para criar a imagem:

```python
fig = plt.figure()
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])
```

Para adicionar um hiperlink à imagem, precisamos usar o método `set_url()` do objeto da imagem. Este método recebe uma URL como seu argumento. Aqui está o código atualizado:

```python
im.set_url('https://www.google.com/')
```

A imagem terá um hiperlink para `https://www.google.com/`. Finalmente, podemos salvar o gráfico como um arquivo SVG usando `fig.savefig()`:

```python
fig.savefig('image.svg')
```
