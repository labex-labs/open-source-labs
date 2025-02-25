# Создать RangeSlider

Теперь мы создадим виджет RangeSlider, который позволит нам настраивать порог изображения. Мы создадим новую ось для ползунка и добавим ее в фигуру.

```python
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())
```
