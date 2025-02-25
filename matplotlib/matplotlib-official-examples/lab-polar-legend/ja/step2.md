# グラフとサブプロットの作成

次に、プロット用のグラフとサブプロットを作成する必要があります。`add_subplot` の `projection` パラメータを使用して、極座標プロットを作成します。

```python
fig = plt.figure()
ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
```
