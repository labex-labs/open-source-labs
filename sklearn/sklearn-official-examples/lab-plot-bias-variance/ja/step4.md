# 比較するモデルを定義する

比較する2つのモデルを定義します。単一の決定木と決定木のバギングアンサンブルです。

```python
estimators = [
    ("Tree", DecisionTreeRegressor()),
    ("Bagging(Tree)", BaggingRegressor(DecisionTreeRegressor())),
]
n_estimators = len(estimators)
```
