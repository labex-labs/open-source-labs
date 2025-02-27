# Définir les classifieurs

Nous allons définir deux classifieurs différents pour comparer leurs performances statistiques pour différents seuils en utilisant les courbes ROC et DET. Nous utiliserons la fonction `make_pipeline` de scikit-learn pour créer un pipeline qui met à l'échelle les données à l'aide de `StandardScaler` et entraîne un classifieur `LinearSVC`. Nous utiliserons également la classe `RandomForestClassifier` de scikit-learn pour entraîner un classifieur forêt aléatoire avec une profondeur maximale de 5, 10 estimateurs et un maximum de 1 caractéristique.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

classifiers = {
    "Linear SVM": make_pipeline(StandardScaler(), LinearSVC(C=0.025, dual="auto")),
    "Random Forest": RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1
    ),
}
```
