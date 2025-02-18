# Définition des données

Nous définissons nos données en utilisant des tuples nommés. Nous définissons un tuple `Student` avec le nom de l'étudiant, sa classe et son genre. Nous définissons également un tuple `Score` avec la valeur du score, l'unité et le percentile.

```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['value', 'unit', 'percentile'])
```
