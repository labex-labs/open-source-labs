# Bibliotheken importieren

Wir beginnen mit dem Import der erforderlichen Bibliotheken. Wir werden die Klassen `Pipeline`, `FeatureUnion`, `GridSearchCV`, `SVC`, `load_iris`, `PCA` und `SelectKBest` aus scikit-learn verwenden.

```python
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
```
