# ライブラリのインポート

必要なライブラリをインポートして始めましょう。scikit - learn の`Pipeline`、`FeatureUnion`、`GridSearchCV`、`SVC`、`load_iris`、`PCA`、および`SelectKBest`クラスを使用します。

```python
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
```
