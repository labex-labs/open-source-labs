# Importez les bibliothèques nécessaires et créez un DataFrame

Pour commencer, nous devons importer les bibliothèques nécessaires - pandas et NumPy. Ensuite, nous allons créer un DataFrame avec quelques valeurs manquantes.

```python
import pandas as pd
import numpy as np

# Créez un DataFrame avec des valeurs manquantes
df = pd.DataFrame(
   np.random.randn(5, 3),
   index=["a", "c", "e", "f", "h"],
   columns=["one", "two", "three"],
)
df["four"] = "bar"
df["five"] = df["one"] > 0
df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
```
