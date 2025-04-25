# サンキー図で 2 つのシステムを接続する

サンキー図では 2 つのシステムを接続することもできます。この例では、接続された 2 つのシステムを持つ図を作成します。

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Two Systems")
flows = [0.25, 0.15, 0.60, -0.10, -0.05, -0.25, -0.15, -0.10, -0.35]
sankey = Sankey(ax=ax, unit=None)
sankey.add(flows=flows, label='one',
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0])
sankey.add(flows=[-0.25, 0.15, 0.1], label='two',
           orientations=[-1, -1, -1], prior=0, connect=(0, 0))
diagrams = sankey.finish()
diagrams[-1].patch.set_hatch('/')
plt.legend()
```

このコードは、接続された 2 つのシステムを持つサンキー図を作成します。生成された図は、タイトル「Two Systems」とともに表示されます。
