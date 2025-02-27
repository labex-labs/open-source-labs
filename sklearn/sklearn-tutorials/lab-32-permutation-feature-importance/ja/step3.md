# モデルの評価

次に、検証セットを使って訓練済みのモデルを評価します。ここで使用する評価指標は決定係数（R-squared score）です。

```python
# Evaluate the model on the validation set
score = model.score(X_val, y_val)
print("Validation score:", score)
```
