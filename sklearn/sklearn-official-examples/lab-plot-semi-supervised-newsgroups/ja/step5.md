# Self-Training モデルの学習と評価

このステップでは、ラベル付きデータの 20% を使って Self-Training を行います。ラベル付きデータの 20% をランダムに選択し、そのデータでモデルを学習させ、そのモデルを使って残りのラベルなしデータのラベルを予測します。

```python
import numpy as np

# 学習データの 20% を選択する
y_mask = np.random.rand(len(y_train)) < 0.2
X_20, y_20 = map(
    list, zip(*((x, y) for x, y, m in zip(X_train, y_train, y_mask) if m))
)

# マスクされていないサブセットをラベルなしに設定する
y_train[~y_mask] = -1

# Self-Training のパイプラインを学習させて評価する
st_pipeline.fit(X_train, y_train)
y_pred = st_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
