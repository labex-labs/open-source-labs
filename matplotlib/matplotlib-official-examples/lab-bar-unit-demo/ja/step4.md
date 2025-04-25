# バーチャートのパラメータを定義する

次のステップは、バーチャートのパラメータを定義することです。グループの x 位置、バーの幅、および x 軸目盛りのラベルを定義します。

```python
ind = np.arange(N)    # the x locations for the groups
width = 0.35         # the width of the bars
ax.set_xticks(ind + width / 2, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
```
