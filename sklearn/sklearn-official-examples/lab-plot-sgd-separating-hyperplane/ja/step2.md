# SGDを使ってSVMモデルを学習する

次に、SGDを使ってSVMモデルを学習する必要があります。Scikit-learnの`SGDClassifier`クラスを使ってモデルを学習します。SVMアルゴリズムを使うために`loss`パラメータを「hinge」に設定し、正則化強度を制御するために`alpha`パラメータを0.01に設定します。また、反復回数を制限するために`max_iter`パラメータを200に設定します。

```python
# fit the model
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
clf.fit(X, Y)
```
