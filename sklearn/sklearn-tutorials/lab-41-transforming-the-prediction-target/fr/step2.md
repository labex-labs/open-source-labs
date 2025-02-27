# Binarisation des multi-étiquettes

La binarisation des multi-étiquettes est le processus de conversion d'une collection de collections d'étiquettes en un format indicateur. Cela peut être réalisé à l'aide de la classe `MultiLabelBinarizer`.

```python
from sklearn.preprocessing import MultiLabelBinarizer

# Définir une liste de collections d'étiquettes
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# Créer une instance de MultiLabelBinarizer et effectuer une transformation d'ajustement sur la liste de collections
MultiLabelBinarizer().fit_transform(y)
```
