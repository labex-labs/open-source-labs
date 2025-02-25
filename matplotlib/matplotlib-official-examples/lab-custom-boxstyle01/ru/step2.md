# Реализация пользовательского стиля рамки в виде класса

Пользовательские стили рамок также можно реализовать в виде классов, которые реализуют `__call__`. Затем классы можно зарегистрировать в словаре `BoxStyle._style_list`, что позволяет указать стиль рамки в виде строки, `bbox=dict(boxstyle="зарегистрированное_имя,параметр=значение,...",...)`.

```python
class MyStyle:
    """Простая рамка."""

    def __init__(self, pad=0.3):
        """
        Аргументы должны быть вещественными числами и иметь значения по умолчанию.

        Параметры
        ----------
        pad : float
            количество отступа
        """
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        """
        Данное расположение и размер рамки, возвращает траекторию рамки вокруг нее.

        Поворот автоматически обрабатывается.

        Параметры
        ----------
        x0, y0, width, height : float
            Расположение и размер рамки.
        mutation_size : float
            Ссылка на масштаб мьютации, обычно размер шрифта текста.
        """
        # отступ
        pad = mutation_size * self.pad
        # ширина и высота с добавленным отступом
        width = width + 2.*pad
        height = height + 2.*pad
        # граница отступленной рамки
        x0, y0 = x0 - pad, y0 - pad
        x1, y1 = x0 + width, y0 + height
        # возвращаем новую траекторию
        return Path([(x0, y0),
                     (x1, y0), (x1, y1), (x0, y1),
                     (x0-pad, (y0+y1)/2.), (x0, y0),
                     (x0, y0)],
                    closed=True)


BoxStyle._style_list["angled"] = MyStyle  # Регистрируем пользовательский стиль.

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))

del BoxStyle._style_list["angled"]  # Удаляем регистрацию.

plt.show()
```
