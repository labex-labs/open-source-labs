# Configurar a figura e os eixos

Criaremos um objeto figura e configuraremos quatro objetos eixos usando o método `fig.add_axes`.

```python
fig = plt.figure(figsize=(5.5, 4))
rect = (0.1, 0.1, 0.8, 0.8)
ax = [fig.add_axes(rect, label="%d" % i) for i in range(4)]
```
