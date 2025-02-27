# Analyse en Composantes Indépendantes (ICA)

#### ICA pour la séparation des sources aveugles

L'Analyse en Composantes Indépendantes (ICA) est utilisée pour séparer des signaux mélangés en leurs composantes source d'origine. Elle suppose que les composantes sont statistiquement indépendantes et peuvent être extraites grâce à un processus de désassemblage linéaire. L'ICA peut être implémentée à l'aide de la classe `FastICA` de scikit-learn.

```python
from sklearn.decomposition import FastICA

# Crée un objet ICA avec n_components comme nombre de composantes souhaitées
ica = FastICA(n_components=2)

# Ajuste le modèle ICA aux signaux mélangés
ica.fit(mixed_signals)

# Sépare les signaux mélangés en leurs composantes source d'origine
source_components = ica.transform(mixed_signals)
```
