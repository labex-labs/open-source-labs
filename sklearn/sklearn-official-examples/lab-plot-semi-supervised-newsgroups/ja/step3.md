# 教師ありモデルの学習と評価

このステップでは、データセットを学習セットとテストセットに分割し、ステップ 2 で作成した教師ありモデルのパイプラインを学習させて評価します。

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# データセットを学習セットとテストセットに分割する
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 教師ありモデルのパイプラインを学習させて評価する
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
