# 予測と精度の測定

入力データのクラスラベルを予測し、分類器の精度を測定します。

```python
y_pred = clf.predict(X)
print("Accuracy: ", np.mean(y == y_pred))
```
