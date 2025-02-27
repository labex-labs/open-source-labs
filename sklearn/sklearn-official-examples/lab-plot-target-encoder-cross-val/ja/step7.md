# 交差検証を用いずに Ridge 回帰モデルを学習させる

`TargetEncoder.fit_transform` は区間交差検証（interval cross-validation）を使用しますが、`TargetEncoder.transform` 自体は交差検証を行いません。これは完全な訓練セットの集計結果を使用してカテゴリ特徴量を変換します。したがって、`TargetEncoder.fit` の後に `TargetEncoder.transform` を使用することで、交差検証を無効にすることができます。このエンコーディング結果を Ridge モデルに渡します。以下のコードを実行して、交差検証を用いずに Ridge モデルを学習させてください。

```python
target_encoder = TargetEncoder(random_state=0)
target_encoder.fit(X_train, y_train)
X_train_no_cv_encoding = target_encoder.transform(X_train)
X_test_no_cv_encoding = target_encoder.transform(X_test)

model_no_cv = ridge.fit(X_train_no_cv_encoding, y_train)
print(
    "Model without CV on training set: ",
    model_no_cv.score(X_train_no_cv_encoding, y_train),
)
print(
    "Model without CV on test set: ", model_no_cv.score(X_test_no_cv_encoding, y_test)
)
```
