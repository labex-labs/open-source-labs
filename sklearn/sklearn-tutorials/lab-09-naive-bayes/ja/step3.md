# ガウスナイーブベイズ分類器の訓練と評価

ここで、学習用セットでガウスナイーブベイズ分類器を訓練し、テスト用セットでその性能を評価します。`sklearn.naive_bayes`モジュールの`GaussianNB`クラスを使用します。

```python
from sklearn.naive_bayes import GaussianNB

# ガウスナイーブベイズ分類器を作成する
gnb = GaussianNB()

# 分類器を訓練する
gnb.fit(X_train, y_train)

# テスト用セットの目的変数を予測する
y_pred = gnb.predict(X_test)

# 分類器の正解率を計算する
accuracy = (y_pred == y_test).sum() / len(y_test)
print("正解率：", accuracy)
```
