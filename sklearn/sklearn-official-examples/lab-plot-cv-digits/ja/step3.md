# テストするハイパーパラメータ値を定義する

正則化パラメータ C の異なる値をテストします。このパラメータは、マージンを最大化することと分類誤差を最小化することのトレードオフを制御します。10^-10 と 1 の間で対数的に等間隔な 10 個の値をテストします。

```python
C_s = np.logspace(-10, 0, 10)
```
