# Konstruktion von nullable Integer-Arrays

Pandas bietet die `IntegerArray`-Klasse zum Erstellen von Arrays mit nullable Ganzzahlen. Lassen Sie uns beginnen, ein `IntegerArray` zu erstellen.

```python
# Importieren der erforderlichen Bibliotheken
import pandas as pd
import numpy as np

# Erstellen eines IntegerArrays mit fehlenden Werten
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
# Ausgabe: <IntegerArray>
# [1, 2, <NA>]
# Länge: 3, dtype: Int64
```

Sie können auch den String-Alias "Int64" verwenden, um den Datentyp anzugeben, wenn das Array erstellt wird. Alle NA-ähnlichen Werte werden durch `pandas.NA` ersetzt.

```python
# Erstellen eines IntegerArrays mit dem String-Alias "Int64"
arr = pd.array([1, 2, np.nan], dtype="Int64")
# Ausgabe: <IntegerArray>
# [1, 2, <NA>]
# Länge: 3, dtype: Int64
```
