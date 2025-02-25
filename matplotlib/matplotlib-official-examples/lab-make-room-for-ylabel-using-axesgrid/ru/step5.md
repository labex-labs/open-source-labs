# Создать место для метки оси Y и настроить оси

В этом шаге мы используем метод `make_axes_area_auto_adjustable`, чтобы создать место для метки оси Y на обеих осях. Также мы используем параметр `use_axes`, чтобы указать оси для настройки, и параметр `pad`, чтобы настроить расстояние между осями.

```python
make_axes_area_auto_adjustable(ax1, pad=0.1, use_axes=[ax1, ax2])
make_axes_area_auto_adjustable(ax2, pad=0.1, use_axes=[ax1, ax2])
```
