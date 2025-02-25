# Создание трехмерного воксельного графика

Теперь мы создаем трехмерный воксельный график с использованием функции `ax.voxels`. Мы передаем `x`, `y`, `z` и `sphere` в качестве параметров. Также добавляем `facecolors` и `edgecolors` с использованием массива `colors`, который мы определили ранее.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
```
