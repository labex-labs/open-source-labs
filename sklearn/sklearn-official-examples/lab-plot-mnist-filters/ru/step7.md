# Визуализация весов

Наконец, мы визуализируем веса первого слоя многослойного персептрона (MLP). Мы создадим сетку из 4x4 подграфиков и отобразим каждый вес в виде изображения в оттенках серого размером 28x28 пикселей.

```python
fig, axes = plt.subplots(4, 4)
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=0.5 * vmin, vmax=0.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
```
