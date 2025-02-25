# Создаем график для отрицательных данных и цветовую шкалу

Мы создаем график для отрицательных данных и добавляем цветовую шкалу к графику с использованием функции `colorbar`. На этот раз мы указываем расположение цветовой шкалы, а также параметры якоря и уменьшения.

```python
# repeat everything above for the negative data
# you can specify location, anchor and shrink the colorbar
neg = plt.imshow(Zneg, cmap='Reds_r', interpolation='none')
plt.colorbar(neg, location='right', anchor=(0, 0.3), shrink=0.7)
```
