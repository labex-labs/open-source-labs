# Создайте класс пользовательских единиц

В этом шаге мы создадим класс пользовательских единиц - `Foo`. Этот класс будет поддерживать преобразование и разные форматы делений шкалы в зависимости от "единицы". Здесь "единица" - это просто скалярный коэффициент преобразования.

```python
class Foo:
    def __init__(self, val, unit=1.0):
        self.unit = unit
        self._val = val * unit

    def value(self, unit):
        if unit is None:
            unit = self.unit
        return self._val / unit
```
