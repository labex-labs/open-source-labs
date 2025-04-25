# シンプルなサンキー図を作成する

まずは、Sankey クラスの使い方を示すシンプルなサンキー図を作成します。

```python
Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("The default settings produce a diagram like this.")
```

このコードは、デフォルト設定でサンキー図を生成します。これには、フローのラベルと方向が含まれます。生成された図は、タイトル「The default settings produce a diagram like this.」とともに表示されます。
