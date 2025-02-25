# Настройка графика

Теперь, когда мы создали базовый график, давайте настроим его, чтобы он был более нагляден. Мы можем добавить заголовок, метки осей и изменить цвет и стиль линии.

```python
# Add title and axis labels
plt.title('Sin Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Change color and style of line
plt.plot(x, y, color='red', linestyle='dashed')
plt.show()
```
