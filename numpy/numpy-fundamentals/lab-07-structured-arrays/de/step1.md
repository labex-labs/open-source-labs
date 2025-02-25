# Erstellen eines strukturierten Arrays

Um ein strukturiertes Array zu erstellen, können wir die `np.array`-Funktion verwenden und den Datentyp über den `dtype`-Parameter angeben. Der Datentyp sollte eine Liste von Tupeln sein, wobei jedes Tupel ein Feld im strukturierten Array darstellt. Jedes Tupel sollte den Feldnamen und den Datentyp des Felds enthalten.

```python
import numpy as np

# Erstellen eines strukturierten Arrays
x = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
