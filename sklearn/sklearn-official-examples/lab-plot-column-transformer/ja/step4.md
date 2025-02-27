# 学習とテスト

学習用データに対してパイプラインを適合させ、`X_test`のトピックを予測するために使用します。その後、パイプラインの性能指標を表示します。

```python
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Classification report:\n\n{}".format(classification_report(y_test, y_pred)))
```
