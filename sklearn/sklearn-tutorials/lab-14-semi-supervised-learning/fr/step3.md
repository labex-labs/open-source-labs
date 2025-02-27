# Propagation d'étiquettes

#### Présentation de l'algorithme de propagation d'étiquettes

La propagation d'étiquettes est un type d'algorithme d'inférence semi-supervisée sur graphe. Elle construit un graphe de similarité sur tous les éléments du jeu de données d'entrée et utilise ce graphe pour propager les étiquettes des données étiquetées vers les données non étiquetées. La propagation d'étiquettes peut être utilisée pour les tâches de classification et prend en charge les méthodes de noyau pour projeter les données dans des espaces dimensionnels alternatifs.

#### Utilisation de la propagation d'étiquettes dans scikit-learn

Dans scikit-learn, deux modèles de propagation d'étiquettes sont disponibles : `LabelPropagation` et `LabelSpreading`. Les deux modèles construisent un graphe de similarité et propagent les étiquettes. Voici un exemple d'utilisation de la propagation d'étiquettes :

```python
from sklearn.semi_supervised import LabelPropagation

# Créez un modèle de propagation d'étiquettes
label_propagation = LabelPropagation()

# Entraînez le modèle de propagation d'étiquettes sur les données étiquetées
label_propagation.fit(X_labeled, y_labeled)

# Prédisez les étiquettes pour de nouveaux échantillons
y_pred = label_propagation.predict(X_test)
```

Dans l'exemple ci-dessus, `X_labeled` et `y_labeled` sont les données étiquetées, et `X_test` sont les nouveaux échantillons à prédire.
