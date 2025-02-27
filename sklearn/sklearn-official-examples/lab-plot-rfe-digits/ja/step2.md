# RFE オブジェクトの作成とデータの適合

次に、RFE クラスのオブジェクトを作成し、それにデータを適合させます。推定器として線形カーネルを持つサポートベクター分類器 (SVC) を使用します。1 回に 1 つの特徴を選択し、1 ステップずつ進めます。

```python
from sklearn.svm import SVC
from sklearn.feature_selection import RFE

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
```
