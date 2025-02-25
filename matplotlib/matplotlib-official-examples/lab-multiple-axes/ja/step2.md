# グラフとサブプロットの作成

2 番目のステップは、アニメーションに使用するグラフとサブプロットを作成することです。この例では、異なるアスペクト比の 2 つのサブプロットを横並びに作成します。左のサブプロットは単位円で、右のサブプロットはサインカーブをアニメーション化するための空のプロットです。

```python
fig, (axl, axr) = plt.subplots(
    ncols=2,
    sharey=True,
    figsize=(6, 2),
    gridspec_kw=dict(width_ratios=[1, 3], wspace=0),
)
axl.set_aspect(1)
axr.set_box_aspect(1 / 3)
axr.yaxis.set_visible(False)
axr.xaxis.set_ticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
```
