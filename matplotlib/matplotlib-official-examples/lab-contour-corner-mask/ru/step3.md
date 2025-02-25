# Маскирование данных

В этом шаге мы замаскируем некоторые значения `z` с использованием булевской маски. Мы создаем массив `mask` с использованием функции `np.zeros_like()`, а затем устанавливаем некоторые значения в `True`, чтобы их замаскировать.

```python
# Mask various z values.
mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)
```
