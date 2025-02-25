# Настраиваем график

Мы можем настроить график, добавив метки к осям x и y, заголовок к графику и легенду. Мы также можем изменить стиль линии и цвет.

```python
plt.plot(x, y, linestyle='--', color='red', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.legend()
```
