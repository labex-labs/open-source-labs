# モデルの学習

L1 ペナルティ付きのロジスティック回帰と SAGA アルゴリズムを使ってモデルを学習します。`C`の値を訓練サンプル数で割った 50.0 に設定します。

```python
# Turn up tolerance for faster convergence
clf = LogisticRegression(C=50.0 / train_samples, penalty="l1", solver="saga", tol=0.1)
clf.fit(X_train, y_train)
```
