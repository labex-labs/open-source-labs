# Увеличить размер воксельного изображения

Теперь мы используем функцию `explode`, определенную ранее, для увеличения размера воксельного изображения, оставляя зазоры между каждым вокселем.

```python
filled = np.ones(n_voxels.shape)
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)
```
