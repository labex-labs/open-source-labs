# Создаем класс AnnotatedCursor

Создадим новый класс `AnnotatedCursor`, который наследуется от `matplotlib.widgets.Cursor` и демонстрирует создание новых виджетов и их обработчиков событий. Класс `AnnotatedCursor` используется для создания курсора в виде крестика с текстом, показывающим текущие координаты.

```python
class AnnotatedCursor(Cursor):
    """
    A crosshair cursor like `~matplotlib.widgets.Cursor` with a text showing \
    the current coordinates.
   ...
    """
```
