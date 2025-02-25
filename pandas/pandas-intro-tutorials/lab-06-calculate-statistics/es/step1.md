# Importando el conjunto de datos

El primer paso es importar el conjunto de datos que usaremos.

```python
# Importando la biblioteca pandas
import pandas as pd

# Leyendo el conjunto de datos
titanic = pd.read_csv("data/titanic.csv")

# Mostrando las primeras cinco filas del conjunto de datos
titanic.head()
```
