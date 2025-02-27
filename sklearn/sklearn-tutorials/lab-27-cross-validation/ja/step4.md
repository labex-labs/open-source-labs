# モデルを学習させて評価する

次に、学習用データセットでサポートベクターマシン（SVM）分類器を学習させ、テスト用データセットでその性能を評価しましょう。

```python
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Accuracy: ", score)
```
