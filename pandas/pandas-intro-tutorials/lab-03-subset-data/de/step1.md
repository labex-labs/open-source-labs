# Importieren der erforderlichen Bibliotheken und Daten

Zunächst müssen wir die Pandas-Bibliothek und das Titanic-Dataset importieren.

```python
# Import pandas library
import pandas as pd

# Load the Titanic dataset
titanic = pd.read_csv("data/titanic.csv")
titanic.head()
```
