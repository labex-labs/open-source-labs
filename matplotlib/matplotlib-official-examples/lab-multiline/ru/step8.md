# Настройка подписей оси X

Для настройки подписей оси X мы можем использовать функцию `set_xticks`. Мы можем указать позиции и метки делений.

```python
ax1.set_xticks([0.2, 0.4, 0.6, 0.8, 1.],
               labels=["Jan\n2009", "Feb\n2009", "Mar\n2009", "Apr\n2009",
                       "May\n2009"])
```
