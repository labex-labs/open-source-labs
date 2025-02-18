# Definieren der Daten

Wir definieren unsere Daten mithilfe von benannten Tupeln (named tuples). Wir definieren ein `Student`-Tupel mit dem Namen, der Klasse und dem Geschlecht des Schülers. Wir definieren auch ein `Score`-Tupel mit dem Punktwert, der Einheit und dem Percentil.

```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['value', 'unit', 'percentile'])
```
