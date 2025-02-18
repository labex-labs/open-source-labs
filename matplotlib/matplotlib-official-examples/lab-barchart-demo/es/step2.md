# Definir los datos

Definimos nuestros datos utilizando tuplas nombradas. Definimos una tupla `Student` con el nombre, la calificación y el género del estudiante. También definimos una tupla `Score` con el valor de la puntuación, la unidad y el percentil.

```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['value', 'unit', 'percentile'])
```
