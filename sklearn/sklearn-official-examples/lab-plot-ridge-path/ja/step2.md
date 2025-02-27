# データを生成する

このステップでは、10x10のヒルベルト行列を生成し、目的変数yを全て1のベクトルに設定します。

```python
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
```
