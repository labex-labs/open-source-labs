# Настройка графика

Мы можем настроить график, настроив базовую линию с использованием параметра `bottom`. Мы также можем настроить свойства формата графика с использованием параметров `linefmt`, `markerfmt` и `basefmt`.

```python
markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1)
markerline.set_markerfacecolor('none')
plt.show()
```

Это сгенерирует график с форматом линии серого цвета и маркерами в виде ромбов. Базовая линия также была настроена на 1,1.
