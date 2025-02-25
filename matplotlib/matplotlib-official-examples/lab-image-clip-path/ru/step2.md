# Загрузка изображения

Мы будем использовать метод `get_sample_data` из `cbook` для загрузки образцового изображения. Этот метод возвращает объект, подобный файлу, который мы можем передать в `imshow` для отображения изображения.

```python
with cbook.get_sample_data('grace_hopper.jpg') as image_file:
    image = plt.imread(image_file)
```
