# Определение данных

Мы определяем наши данные с использованием именованных кортежей (named tuples). Мы определяем кортеж `Student` с именем студента, классом и полом. Также мы определяем кортеж `Score` со значением оценки, единицей измерения и процентилем.

```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['value', 'unit', 'percentile'])
```
