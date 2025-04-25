# アルファの定義

正則化パラメータである alpha の異なる値を定義します。0.1 と 10 の間で対数的に等間隔な 5 つの値を生成するために np.logspace を使用します。

```python
alphas = np.logspace(-1, 1, 5)
```
