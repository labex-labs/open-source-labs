# パイプラインを評価する

このステップでは、モデルのスコアを計算することでパイプラインの性能を評価します。

```python
print("model score: %.3f" % clf.score(X_test, y_test))
```
