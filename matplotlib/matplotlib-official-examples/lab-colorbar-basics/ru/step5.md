# Создаем график с положительными и отрицательными данными

Мы создаем график с обоими положительными и отрицательными данными и добавляем цветовую шкалу к графику с использованием функции `colorbar`. На этот раз мы указываем минимальные и максимальные значения для цветовой шкалы с использованием параметров `vmin` и `vmax`.

```python
# Plot both positive and negative values between +/- 1.2
pos_neg_clipped = plt.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2,
                             interpolation='none')

# Add minorticks on the colorbar to make it easy to read the
# values off the colorbar.
cbar = plt.colorbar(pos_neg_clipped, extend='both')
cbar.minorticks_on()
```
