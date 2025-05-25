# Visualizar Pesos

Finalmente, visualizaremos os pesos da primeira camada do MLP. Criaremos uma grade de 4x4 de subplots e exibiremos cada peso como uma imagem em escala de cinza de 28x28 pixels.

```python
fig, axes = plt.subplots(4, 4)
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=0.5 * vmin, vmax=0.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
```
