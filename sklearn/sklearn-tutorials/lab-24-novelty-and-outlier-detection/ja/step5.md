# アウトライアを予測する

モデルが適合させられたら、新しい観測値がアウトライアかどうかを予測するために`predict`メソッドを使用できます。`predict`メソッドは、内包値に対しては1を、アウトライアに対しては-1を返します。

```python
X_test = [5.5, 8.5]
predictions = estimator.predict(X_test)
print(predictions)
```
