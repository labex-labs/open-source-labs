# Построение гистограммы интенсивности МРТ

Далее мы построим гистограмму интенсивности МРТ с использованием функции `hist()`. Мы нормализуем значения интенсивности в диапазоне от 0 до 1.

```python
# Plot the histogram of MRI intensity
ax1 = fig.add_subplot(2, 2, 2)
im = np.ravel(im)
im = im[np.nonzero(im)]  # Игнорируем фон
im = im / im.max()  # Нормализация
ax1.hist(im, bins=100)
ax1.set_xlabel('Intensity (a.u.)')
ax1.set_ylabel('MRI density')
```
