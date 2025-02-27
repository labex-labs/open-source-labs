# FeatureHasher

Nous allons évaluer `FeatureHasher`, qui est une méthode qui construit un vecteur de longueur prédéfinie en appliquant une fonction de hachage aux caractéristiques (par exemple, les jetons), puis en utilisant directement les valeurs de hachage comme indices de caractéristiques et en mettant à jour le vecteur résultant à ces indices.

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

t0 = time()
hasher = FeatureHasher(n_features=2**18)
X = hasher.transform(token_freqs(d) for d in raw_data)
duration = time() - t0
print(f"terminé en {duration:.3f} s")
print(f"Trouvé {len(np.unique(X.nonzero()[1]))} jetons uniques")
```
