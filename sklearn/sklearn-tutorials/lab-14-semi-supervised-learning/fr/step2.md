# Auto-apprentissage

#### Présentation de l'algorithme d'auto-apprentissage

L'algorithme d'auto-apprentissage est basé sur l'algorithme de Yarowsky. Il permet à un classifieur supervisé de fonctionner comme un classifieur semi-supervisé en apprenant à partir de données non étiquetées. L'algorithme fonctionne en entraînant itérativement le classifieur supervisé sur les données étiquetées et non étiquetées, puis en utilisant les prédictions sur les données non étiquetées pour ajouter un sous-ensemble de ces échantillons aux données étiquetées. L'algorithme continue d'itérer jusqu'à ce que tous les échantillons aient des étiquettes ou qu'aucun nouvel échantillon ne soit sélectionné lors d'une itération.

#### Utilisation de l'auto-apprentissage dans scikit-learn

Dans scikit-learn, l'algorithme d'auto-apprentissage est implémenté dans la classe `SelfTrainingClassifier`. Pour utiliser cet algorithme, vous devez fournir un classifieur supervisé qui implémente la méthode `predict_proba`. Voici un exemple d'utilisation de l'algorithme d'auto-apprentissage :

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.linear_model import LogisticRegression

# Créez un classifieur de régression logistique
classifier = LogisticRegression()

# Créez un classifieur d'auto-apprentissage avec le classifieur de régression logistique comme classifieur de base
self_training_classifier = SelfTrainingClassifier(classifier)

# Entraînez le classifieur d'auto-apprentissage sur les données étiquetées et non étiquetées
self_training_classifier.fit(X_labeled, y_labeled, X_unlabeled)

# Prédisez les étiquettes pour de nouveaux échantillons
y_pred = self_training_classifier.predict(X_test)
```

Dans l'exemple ci-dessus, `X_labeled` et `y_labeled` sont les données étiquetées, `X_unlabeled` sont les données non étiquetées et `X_test` sont les nouveaux échantillons à prédire.
