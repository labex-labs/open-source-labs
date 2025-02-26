# Подготовка

Одной из потенциально раздражающих сторон пакетов является то, что они усложняют инструкции по импорту. Например, в программе `stock.py` теперь есть инструкции по импорту, такие как следующие:

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

Если пакет предназначен для использования в целом, то может быть более разумным (и проще) объединить все в единый верхний уровень пакета. Давайте это сделаем:
