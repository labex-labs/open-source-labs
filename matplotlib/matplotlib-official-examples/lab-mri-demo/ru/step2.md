# Загрузить данные изображения с магнитно-резонансной томографии (МРТ)

Мы будем использовать функцию `get_sample_data` из `matplotlib` для загрузки образца изображения с МРТ. Изображение имеет формат 16-разрядных целых чисел размером 256x256.

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```
