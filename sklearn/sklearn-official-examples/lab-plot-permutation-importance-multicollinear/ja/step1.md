# ランダムフォレスト分類器を学習する

まず、ウィスコンシン乳がんデータセットを読み込み、学習用とテスト用のセットに分割します。その後、学習用セットでランダムフォレスト分類器を学習し、テスト用セットでの精度を評価します。

```python
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print("Accuracy on test data: {:.2f}".format(clf.score(X_test, y_test)))
```
