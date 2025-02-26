# Préparation

Un aspect potentiellement gênant des packages est qu'ils compliquent les instructions d'importation. Par exemple, dans le programme `stock.py`, vous avez maintenant des instructions d'importation telles que les suivantes :

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

Si le package est destiné à être utilisé comme un tout unifié, il peut être plus sage (et plus facile) de regrouper tout dans un seul package de niveau supérieur. Faisons-le :
