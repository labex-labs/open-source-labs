# モデルの定義

このステップでは、ベルヌーイ RBM 特徴抽出器とロジスティック回帰分類器を使用して分類パイプラインを定義します。それぞれ `sklearn.neural_network` と `sklearn.linear_model` モジュールから `BernoulliRBM` と `LogisticRegression` クラスを使用します。その後、2 つのモデルを結合するためのパイプラインオブジェクト `rbm_features_classifier` を作成します。

```python
from sklearn import linear_model
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

logistic = linear_model.LogisticRegression(solver="newton-cg", tol=1)
rbm = BernoulliRBM(random_state=0, verbose=True)

rbm_features_classifier = Pipeline(steps=[("rbm", rbm), ("logistic", logistic)])
```
