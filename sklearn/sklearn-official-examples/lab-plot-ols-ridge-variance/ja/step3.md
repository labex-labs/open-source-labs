# 識別器の定義

このステップでは、OLSとリッジ回帰の識別器を定義します。

```python
classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)
```
