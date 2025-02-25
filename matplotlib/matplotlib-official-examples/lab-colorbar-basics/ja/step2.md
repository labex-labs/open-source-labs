# データを生成する

`numpy` の `mgrid` 関数を使って、プロットするサンプルデータを生成します。

```python
# setup some generic data
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))
```
