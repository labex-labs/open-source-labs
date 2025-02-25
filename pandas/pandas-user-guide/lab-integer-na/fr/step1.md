# Construction d'objets `IntegerArray` avec des valeurs manquantes

Pandas fournit la classe `IntegerArray` pour créer des tableaux d'entiers pouvant contenir des valeurs manquantes. Commençons par créer un `IntegerArray`.

```python
# Importez les bibliothèques nécessaires
import pandas as pd
import numpy as np

# Créez un `IntegerArray` avec des valeurs manquantes
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
# Sortie : <IntegerArray>
# [1, 2, <NA>]
# Longueur : 3, dtype : Int64
```

Vous pouvez également utiliser l'alias de chaîne de caractères "Int64" pour spécifier le type de données lors de la création du tableau. Toutes les valeurs du type NA sont remplacées par `pandas.NA`.

```python
# Créez un `IntegerArray` en utilisant l'alias de chaîne de caractères "Int64"
arr = pd.array([1, 2, np.nan], dtype="Int64")
# Sortie : <IntegerArray>
# [1, 2, <NA>]
# Longueur : 3, dtype : Int64
```
