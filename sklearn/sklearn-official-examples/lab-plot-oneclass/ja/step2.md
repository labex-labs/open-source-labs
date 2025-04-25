# 1 クラス SVM モデルをフィットさせる

次に、生成したデータに 1 クラス SVM モデルをフィットさせます。

```python
# モデルをフィットさせる
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# 学習データ、通常の新奇な観測値、および異常な新奇な観測値に対するラベルを予測する
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
```
