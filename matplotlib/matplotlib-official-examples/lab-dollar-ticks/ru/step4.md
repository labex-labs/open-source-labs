# Настройка параметров делений

Мы также можем настроить параметры делений, чтобы дополнительно изменить внешний вид нашего графика. В этом примере мы изменим цвет меток делений на зеленый и переместим их на правую сторону графика.

```python
# Customize tick parameters
ax.tick_params(axis='y', which='major', labelcolor='green', labelright=True)
```

В приведенном выше коде мы используем метод `tick_params` для настройки параметров делений по оси Y. Мы устанавливаем параметр `axis` в значение `'y'`, чтобы указать, что настраиваем оси Y, и параметр `which` в значение `'major'`, чтобы указать, что настраиваем основные деления. Мы устанавливаем параметр `labelcolor` в значение `'green'`, чтобы изменить цвет меток делений, и параметр `labelright` в значение `True`, чтобы переместить метки делений на правую сторону графика.
