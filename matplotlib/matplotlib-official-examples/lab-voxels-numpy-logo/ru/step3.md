# Построить логотип NumPy

Теперь мы можем начать строить логотип NumPy с использованием трехмерного NumPy-массива под названием `n_voxels`. Мы устанавливаем некоторые элементы в массиве в значение True, чтобы представить форму логотипа. Также мы определяем два других NumPy-массива под названием `facecolors` и `edgecolors`, которые будут использоваться для окрашивания вокселей.

```python
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True

facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
```
