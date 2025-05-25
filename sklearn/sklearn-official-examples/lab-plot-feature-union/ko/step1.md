# 라이브러리 가져오기

필요한 라이브러리를 가져오는 것으로 시작합니다. scikit-learn 의 `Pipeline`, `FeatureUnion`, `GridSearchCV`, `SVC`, `load_iris`, `PCA`, 그리고 `SelectKBest` 클래스를 사용할 것입니다.

```python
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
```
