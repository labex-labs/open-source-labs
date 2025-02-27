# Загрузка набора данных

В этом шаге мы загрузим набор данных digits из scikit - learn. Этот набор данных содержит изображения рукописных цифр от 0 до 9.

```python
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
```
