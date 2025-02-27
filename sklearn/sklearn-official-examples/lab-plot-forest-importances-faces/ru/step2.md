# Оценка важности признаков

Мы оцениваем важность признаков на основе среднего уменьшения нечистоты (MDI). Важность признаков предоставляется атрибутом `feature_importances_` обученной модели, и они вычисляются как среднее и стандартное отклонение накопления уменьшения нечистоты внутри каждого дерева.

```python
import time
import matplotlib.pyplot as plt

start_time = time.time()
img_shape = data.images[0].shape
importances = forest.feature_importances_
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")
imp_reshaped = importances.reshape(img_shape)
plt.matshow(imp_reshaped, cmap=plt.cm.hot)
plt.title("Pixel importances using impurity values")
plt.colorbar()
plt.show()
```
