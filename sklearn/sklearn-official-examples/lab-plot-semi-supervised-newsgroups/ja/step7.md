# LabelSpreading モデルの学習と評価

このステップでは、ラベル付きデータの 20% を使って LabelSpreading を行います。ラベル付きデータの 20% をランダムに選択し、そのデータでモデルを学習させ、そのモデルを使って残りのラベルなしデータのラベルを予測します。

```python
# LabelSpreading のパイプラインを学習させて評価する
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
