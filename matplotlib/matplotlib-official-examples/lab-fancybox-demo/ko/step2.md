# Fancybox 를 사용하여 샘플 상자 플로팅

이 단계에서는 1 단계에서 얻은 상자 스타일을 사용하여 fancybox 를 갖는 샘플 상자를 플로팅합니다.

```python
ncol = 2
nrow = (len(styles) + 1) // ncol
axs = (plt.figure(figsize=(3 * ncol, 1 + nrow))
       .add_gridspec(1 + nrow, ncol, wspace=.5).subplots())

for ax in axs.flat:
    ax.set_axis_off()

for ax in axs[0, :]:
    ax.text(.2, .5, "boxstyle",
            transform=ax.transAxes, size="large", color="tab:blue",
            horizontalalignment="right", verticalalignment="center")
    ax.text(.4, .5, "default parameters",
            transform=ax.transAxes,
            horizontalalignment="left", verticalalignment="center")

for ax, (stylename, stylecls) in zip(axs[1:, :].T.flat, styles.items()):
    ax.text(.2, .5, stylename, bbox=dict(boxstyle=stylename, fc="w", ec="k"),
            transform=ax.transAxes, size="large", color="tab:blue",
            horizontalalignment="right", verticalalignment="center")
    ax.text(.4, .5, str(inspect.signature(stylecls))[1:-1].replace(", ", "\n"),
            transform=ax.transAxes,
            horizontalalignment="left", verticalalignment="center")
```
