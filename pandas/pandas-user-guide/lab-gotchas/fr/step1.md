# Comprendre l'utilisation mémoire des DataFrame

Pandas fournit plusieurs méthodes pour comprendre l'utilisation mémoire d'un DataFrame. La méthode `.info()` peut être utilisée pour voir un résumé, y compris l'utilisation mémoire.

```python
import pandas as pd
import numpy as np

# Créer un DataFrame
dtypes = ["int64", "float64", "datetime64[ns]", "timedelta64[ns]", "complex128", "object", "bool"]
n = 5000
data = {t: np.random.randint(100, size=n).astype(t) for t in dtypes}
df = pd.DataFrame(data)
df["categorical"] = df["object"].astype("category")

# Afficher les informations du DataFrame
df.info()
```
