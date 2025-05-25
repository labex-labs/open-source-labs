# Importar Bibliotecas

Começaremos importando as bibliotecas necessárias. Usaremos as classes `Pipeline`, `FeatureUnion`, `GridSearchCV`, `SVC`, `load_iris`, `PCA` e `SelectKBest` do `scikit-learn`.

```python
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
```
