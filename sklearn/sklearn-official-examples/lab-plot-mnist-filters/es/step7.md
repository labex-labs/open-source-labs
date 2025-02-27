# Visualizar pesos

Finalmente, visualizaremos los pesos de la primera capa de la MLP. Crearemos una cuadrícula de subtramas de 4x4 y mostraremos cada peso como una imagen en escala de grises de 28x28 píxeles.

```python
fig, axes = plt.subplots(4, 4)
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=0.5 * vmin, vmax=0.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
```
