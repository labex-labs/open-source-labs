# API Challenge: Type hints

Funktionen können optionale Typhinweise an Argumente und Rückgabewerte angehängt werden. Beispielsweise:

```python
def add(x:int, y:int) -> int:
    return x + y
```

Das Modul `typing` hat zusätzliche Klassen für das Ausdrücken von komplexeren Typen, einschließlich Container. Beispielsweise:

```python
from typing import List

def sum_squares(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n*n
    return total
```

Ihre Herausforderung: Ändern Sie den Code in `reader.py`, sodass alle Funktionen Typhinweise haben. Versuchen Sie, die Typhinweise so genau wie möglich zu gestalten. Dazu können Sie eventuell die Dokumentation für das [typing-Modul](https://docs.python.org/3/library/typing.html) konsultieren.
