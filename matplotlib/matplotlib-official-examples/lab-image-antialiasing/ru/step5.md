# Пересэмплирование изображения с использованием интерполяции "antialiased"

Наконец, мы увеличим разрешение изображения от 500 пикселей до 530 пикселей для отображения с использованием интерполяции "antialiased". Это покажет, как использование более качественных алгоритмов антиалиасинга может уменьшить эффект Моира.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='antialiased', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='antialiased'")
plt.show()
```
