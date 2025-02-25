# Stockage de données textuelles

En pandas, vous pouvez stocker des données textuelles de deux manières : en utilisant un tableau NumPy de type `object` ou un type d'extension `StringDtype`. Nous recommandons d'utiliser `StringDtype` car il est plus sécuritaire et plus spécifique que le type générique `object`.

```python
import pandas as pd

# créer une série avec le type `object`
s1 = pd.Series(["a", "b", "c"], dtype="object")

# créer une série avec `StringDtype`
s2 = pd.Series(["a", "b", "c"], dtype="string")
```
