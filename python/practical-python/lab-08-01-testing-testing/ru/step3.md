# Встроенные тесты

Утверждения также могут использоваться для простых тестов.

```python
def add(x, y):
    return x + y

assert add(2,2) == 4
```

Таким образом, вы включаете тест в ту же модуль, что и ваш код.

_Преимущество: Если код явно сломан, попытки импортировать модуль будут приводить к ошибке._

Это не рекомендуется для исчерпывающего тестирования. Это скорее базовый "тест на冒烟". Работает ли функция вообще на любом примере? Если нет, то что-то явно сломано.
