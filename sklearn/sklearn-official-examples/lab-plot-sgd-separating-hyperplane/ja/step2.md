# SGD を使って SVM モデルを学習する

次に、SGD を使って SVM モデルを学習する必要があります。Scikit-learn の`SGDClassifier`クラスを使ってモデルを学習します。SVM アルゴリズムを使うために`loss`パラメータを「hinge」に設定し、正則化強度を制御するために`alpha`パラメータを 0.01 に設定します。また、反復回数を制限するために`max_iter`パラメータを 200 に設定します。

```python
# fit the model
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
clf.fit(X, Y)
```
