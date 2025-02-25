# 制約付きレイアウトを使用したネストされたグリッドスペックの作成

制約付きレイアウトを持つネストされたグリッドスペックを使用して、より複雑な例を作成します。これにより、サブプロットのレイアウトをより細かく制御することができます。

```python
fig = plt.figure(layout='constrained')

gs0 = gridspec.GridSpec(1, 2, figure=fig)

gs1 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=gs0[0])
for n in range(3):
    ax = fig.add_subplot(gs1[n])
    example_plot(ax)


gs2 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs0[1])
for n in range(2):
    ax = fig.add_subplot(gs2[n])
    example_plot(ax)

plt.show()
```
