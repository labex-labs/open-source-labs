# Инструкция `import as`

Вы можете изменить имя модуля при импорте:

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

Это работает так же, как обычный импорт. Просто переименовывает модуль в этом файле.
