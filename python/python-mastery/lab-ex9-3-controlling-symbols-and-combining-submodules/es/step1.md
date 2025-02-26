# Preparación

Un aspecto potencialmente molesto de los paquetes es que complican las declaraciones de importación. Por ejemplo, en el programa `stock.py`, ahora tienes declaraciones de importación como las siguientes:

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

Si el paquete se pretende utilizar como un todo unificado, puede ser más sensato (y más fácil) consolidar todo en un solo paquete de nivel superior. Hagamos eso:
