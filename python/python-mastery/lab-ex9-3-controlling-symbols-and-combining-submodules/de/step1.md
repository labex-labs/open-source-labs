# Vorbereitung

Ein potenziell störender Aspekt von Paketen ist, dass sie die Importanweisungen komplizieren. Beispielsweise haben Sie in der `stock.py`-Programm jetzt Importanweisungen wie die folgenden:

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

Wenn das Paket als einheitliche Einheit verwendet werden soll, kann es vernünftiger (und einfacher) sein, alles in ein einzelnes oberstes Paket zusammenzufassen. Machen wir das:
