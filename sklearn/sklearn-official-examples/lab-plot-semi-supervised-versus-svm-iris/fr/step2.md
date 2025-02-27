# Configurer les classifieurs Label Spreading

Nous allons configurer trois classifieurs Label Spreading avec différents pourcentages de données étiquetées : 30 %, 50 % et 100 %. Label Spreading est un algorithme d'apprentissage semi-supervisé qui propage les étiquettes des points de données étiquetés vers les points de données non étiquetés sur la base de leur similarité.

```python
from sklearn.semi_supervised import LabelSpreading

# Configurer les classifieurs Label Spreading
rng = np.random.RandomState(0)
y_rand = rng.rand(y.shape[0])
y_30 = np.copy(y)
y_30[y_rand < 0.3] = -1  # définir des échantillons aléatoires comme non étiquetés
y_50 = np.copy(y)
y_50[y_rand < 0.5] = -1
ls30 = (LabelSpreading().fit(X, y_30), y_30, "Label Spreading 30% des données")
ls50 = (LabelSpreading().fit(X, y_50), y_50, "Label Spreading 50% des données")
ls100 = (LabelSpreading().fit(X, y), y, "Label Spreading 100% des données")
```
