# Обучение словаря изображений

Мы используем MiniBatchKMeans для обучения словаря изображений. Мы задаем количество кластеров равным 81, устанавливаем случайное состояние и включаем подробный режим. Затем мы создаем буфер для хранения патчей и перебираем каждое изображение в наборе данных. Мы извлекаем 50 патчей из каждого изображения и преобразуем данные. Затем мы добавляем данные в буфер и увеличиваем индекс. Если индекс кратен 10, мы объединяем буфер и запускаем partial_fit на данных. Если индекс кратен 100, мы выводим сообщение с указанием количества уже обученных патчей.

```python
import time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.image import extract_patches_2d

print("Learning the dictionary... ")
rng = np.random.RandomState(0)
kmeans = MiniBatchKMeans(n_clusters=81, random_state=rng, verbose=True, n_init=3)
patch_size = (20, 20)

buffer = []
t0 = time.time()

# The online learning part: cycle over the whole dataset 6 times
index = 0
for _ in range(6):
    for img in faces.images:
        data = extract_patches_2d(img, patch_size, max_patches=50, random_state=rng)
        data = np.reshape(data, (len(data), -1))
        buffer.append(data)
        index += 1
        if index % 10 == 0:
            data = np.concatenate(buffer, axis=0)
            data -= np.mean(data, axis=0)
            data /= np.std(data, axis=0)
            kmeans.partial_fit(data)
            buffer = []
        if index % 100 == 0:
            print("Partial fit of %4i out of %i" % (index, 6 * len(faces.images)))

dt = time.time() - t0
print("done in %.2fs." % dt)
```
