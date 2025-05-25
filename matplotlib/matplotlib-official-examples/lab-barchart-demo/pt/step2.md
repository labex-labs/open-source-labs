# Definir os Dados

Definimos nossos dados usando tuplas nomeadas. Definimos uma tupla `Student` com o nome, a série e o gênero do aluno. Também definimos uma tupla `Score` com o valor da pontuação, a unidade e o percentil.

```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['value', 'unit', 'percentile'])
```
