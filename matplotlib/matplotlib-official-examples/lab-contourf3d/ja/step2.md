# グラフと軸のオブジェクトを作成する

ここでは、`add_subplot()` メソッドを使ってグラフと軸のオブジェクトを作成します。3D プロットを作成するには、`projection` パラメータを `'3d'` に設定します。

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
```
