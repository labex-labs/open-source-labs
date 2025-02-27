# 交差検証を用いて Ridge 回帰モデルを学習させる

次に、`TargetEncoder` と Ridge モデルを含むパイプラインを作成します。このパイプラインは交差検証を使用する `TargetEncoder.fit_transform` を利用します。以下のコードを実行して、交差検証を用いて Ridge モデルを学習させてください。

```python
model_with_cv = make_pipeline(TargetEncoder(random_state=0), ridge)
model_with_cv.fit(X_train, y_train)
print("Model with CV on training set: ", model_with_cv.score(X_train, y_train))
print("Model with CV on test set: ", model_with_cv.score(X_test, y_test))
```
