# モデルの訓練

線形カーネルを使用してサポートベクターマシン（SVM）分類器を訓練します。結果に与える影響を見るために、正則化パラメータCを非常に低く設定します。

```python
classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
```
