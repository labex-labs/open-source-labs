# Encodage des étiquettes

L'encodage des étiquettes est le processus de conversion d'étiquettes non numériques en étiquettes numériques. Cela peut être réalisé à l'aide de la classe `LabelEncoder`.

```python
from sklearn import preprocessing

# Crée une instance de LabelEncoder
le = preprocessing.LabelEncoder()

# Ajuste le LabelEncoder sur une liste d'étiquettes non numériques
le.fit(["paris", "paris", "tokyo", "amsterdam"])

# Obtenir les classes apprises par le LabelEncoder
list(le.classes_)

# Transforme une liste d'étiquettes non numériques en étiquettes numériques
le.transform(["tokyo", "tokyo", "paris"])

# Inverse la transformation des étiquettes numériques pour les ramener à des étiquettes non numériques
list(le.inverse_transform([2, 2, 1]))
```
