# 新しい Figure と Axes を作成する

最初のステップは、新しい Figure とそれを埋め尽くす Axes を作成することです。これが、シミュレーションが描画されるキャンバスになります。

```python
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
```
