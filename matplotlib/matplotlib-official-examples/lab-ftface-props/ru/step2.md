# Загружаем шрифт

В этом шаге мы загружаем шрифт, с которым будем работать. Мы будем использовать шрифт, поставляемый вместе с Matplotlib.

```python
font = ft.FT2Font(
    os.path.join(matplotlib.get_data_path(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))
```
