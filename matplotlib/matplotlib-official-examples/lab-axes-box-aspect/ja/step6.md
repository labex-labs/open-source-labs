# 多数のサブプロットのボックスアスペクト

初期化時にボックスアスペクトをAxesに渡すことができます。次のコードは、すべての正方形のAxesを持つ2×3のサブプロットグリッドを作成します。

```python
fig7, axs = plt.subplots(2, 3, subplot_kw=dict(box_aspect=1),
                         sharex=True, sharey=True, layout="constrained")

for i, ax in enumerate(axs.flat):
    ax.scatter(i % 3, -((i // 3) - 0.5)*200, c=[plt.cm.hsv(i / 6)], s=300)
plt.show()
```
