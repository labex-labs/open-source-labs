# Настройка оси z

```python
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
```

Мы настраиваем ось z с использованием функции `set_zlim()` для установки пределов оси z в диапазоне от -1.01 до 1.01. Затем мы используем функцию `set_major_locator()` для установки количества делений на оси z в 10 с использованием `LinearLocator(10)`. Наконец, мы используем функцию `set_major_formatter()` для форматирования меток делений оси z с использованием `StrMethodFormatter`.
