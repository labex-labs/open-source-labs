# Преобразование изображения в числа с плавающей точкой и изменение формы

Мы преобразуем изображение в числа с плавающей точкой и изменим его форму на 2D-массив NumPy, чтобы его можно было обработать с использованием алгоритма K-Means.

```python
# Convert to floats instead of the default 8 bits integer coding.
china = np.array(china, dtype=np.float64) / 255

# Get the dimensions of the image
w, h, d = original_shape = tuple(china.shape)
assert d == 3

# Reshape the image into a 2D numpy array
image_array = np.reshape(china, (w * h, d))
```
