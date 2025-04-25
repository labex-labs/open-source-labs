# 早期終了付きでモデルを構築して訓練する

ここでは、早期終了付きで勾配ブースティングモデルを構築して訓練します。検証用の割合（validation*fraction）を指定します。これは、モデルの検証損失を評価するために訓練から取り除かれる全体のデータセットの割合を示します。勾配ブースティングモデルは訓練セットを使って訓練され、検証セットを使って評価されます。回帰木の追加の各段階が追加されるたびに、検証セットを使ってモデルのスコア付けが行われます。これは、最後の n_iter_no_change 段階でのモデルのスコアが少なくとも tol だけ改善しなくなるまで続けられます。その後、モデルは収束したと見なされ、さらなる段階の追加は「早期に停止」されます。最終モデルの段階数は属性 n_estimators*で利用できます。

```python
gbes = ensemble.GradientBoostingClassifier(
        n_estimators=n_estimators,
        validation_fraction=0.2,
        n_iter_no_change=5,
        tol=0.01,
        random_state=0,
    )
start = time.time()
gbes.fit(X_train, y_train)
time_gbes.append(time.time() - start)
```
