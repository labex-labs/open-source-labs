# Preparation

One potentially annoying aspect of packages is that they complicate
import statements. For example, in the `stock.py` program, you now
have import statements such as the following:

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

If the package is meant to be used as a unified whole, it might be
more sane (and easier) to consolidate everything into a single top
level package. Let's do that:
