# Отображение логотипов

В этом шаге мы отобразим логотипы Matplotlib различных размеров.

```python
# Большой логотип:
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7])

# Маленький логотип размером 32 пикселя:
make_logo(height_px=32, lw_bars=0.3, lw_grid=0.3, lw_border=0.3, rgrid=[5])

# Большой логотип с текстом, как используется на сайте Matplotlib.
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7], with_text=True)
plt.show()
```
