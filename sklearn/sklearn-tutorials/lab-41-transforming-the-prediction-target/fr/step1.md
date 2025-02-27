# Binarisation des étiquettes

La binarisation des étiquettes est le processus de conversion d'étiquettes multiclasse en une matrice d'indicateurs binaires. Cela peut être réalisé à l'aide de la classe `LabelBinarizer`.

```python
from sklearn import preprocessing

# Crée une instance de LabelBinarizer
lb = preprocessing.LabelBinarizer()

# Ajuste le LabelBinarizer sur une liste d'étiquettes multiclasse
lb.fit([1, 2, 6, 4, 2])

# Obtenir les classes apprises par le LabelBinarizer
lb.classes_

# Transforme une liste d'étiquettes multiclasse en une matrice d'indicateurs binaires
lb.transform([1, 6])
```
