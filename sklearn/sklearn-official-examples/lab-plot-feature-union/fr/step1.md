# Importation des bibliothèques

Nous allons commencer par importer les bibliothèques requises. Nous utiliserons les classes `Pipeline`, `FeatureUnion`, `GridSearchCV`, `SVC`, `load_iris`, `PCA` et `SelectKBest` de scikit-learn.

```python
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
```
