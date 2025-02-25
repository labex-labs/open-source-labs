# Отобразить изображение и его гистограмму

Далее мы отобразим изображение с использованием функции `imshow` из Matplotlib, а также его гистограмму с использованием `hist`. Мы создадим фигуру с двумя подграфиками, один для изображения, а другой для гистограммы.

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histogram of pixel intensities')
```
