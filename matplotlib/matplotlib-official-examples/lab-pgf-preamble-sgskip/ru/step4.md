# Настройка вида графика

Вы можете настроить вид графика, изменив цвета, стили линий и маркеры. Вот пример:

```python
plt.plot(x, y1, 'r--', label='sin')
plt.plot(x, y2, 'g:', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```
