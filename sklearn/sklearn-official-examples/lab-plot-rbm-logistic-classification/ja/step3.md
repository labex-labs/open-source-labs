# 学習

このステップでは、前のステップで定義したパイプラインモデルを学習します。モデルのハイパーパラメータ（学習率、隠れ層のサイズ、正則化）を設定した後、学習データをモデルに適合させます。

```python
from sklearn.base import clone

# ハイパーパラメータ。これらは GridSearchCV を使った交差検証によって設定されました。
# ここでは時間を節約するために交差検証を行っていません。
rbm.learning_rate = 0.06
rbm.n_iter = 10

# より多くのコンポーネントがより良い予測性能をもたらす傾向がありますが、
# 学習時間は長くなります
rbm.n_components = 100
logistic.C = 6000

# RBM-Logistic パイプラインの学習
rbm_features_classifier.fit(X_train, Y_train)
```
