# データを生成する

このステップでは、10x10 のヒルベルト行列を生成し、目的変数 y を全て 1 のベクトルに設定します。

```python
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
```
