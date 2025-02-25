# Настроить диаграмму

Чтобы сделать диаграмму более информативной, мы можем настроить ее, добавив метки, заголовок и инвертировав ось y.

```python
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # метки читаются сверху вниз
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
```
