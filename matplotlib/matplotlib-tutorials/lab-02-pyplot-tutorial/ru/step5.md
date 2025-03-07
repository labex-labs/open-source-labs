# Настройка свойств линии

Matplotlib позволяет настраивать различные свойства линии, такие как толщина линии, стиль пунктира и цвет. Рассмотрим способы настройки свойств линии:

```python
x = np.arange(0, 5, 0.1)
line, = plt.plot(x, np.sin(x), '-')

# Использование сеттер-метода экземпляра Line2D
line.set_linewidth(2.0)  # Установка свойства толщины линии в 2.0

# Использование функции plt.setp
plt.setp(line, color='r', linewidth=2.0)  # Установка свойств цвета и толщины линии с использованием функции setp

plt.show()
```

Пояснение:

- Мы создаем массив `x` и вычисляем соответствующие значения y с использованием функции `np.sin`.
- Функция `plot` вызывается для создания линейного графика.
- Мы используем метод `set` экземпляра `Line2D` для установки свойства толщины линии в 2.0.
- Альтернативно мы можем использовать функцию `setp` для установки нескольких свойств линии, таких как цвет и толщина линии, с использованием именованных аргументов.
