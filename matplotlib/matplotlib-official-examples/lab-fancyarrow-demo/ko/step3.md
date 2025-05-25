# Figure 설정

`plt.figure()`와 `add_gridspec()`을 사용하여 figure 를 설정합니다. figure 는 2 개의 열과 n 개의 행으로 구성된 그리드를 갖습니다. 여기서 n 은 화살표 스타일의 수입니다. 그리드의 각 셀에는 화살표 스타일과 기본 매개변수가 포함됩니다.

```python
ncol = 2
nrow = (len(styles) + 1) // ncol
axs = (plt.figure(figsize=(4 * ncol, 1 + nrow))
       .add_gridspec(1 + nrow, ncol,
                     wspace=.7, left=.1, right=.9, bottom=0, top=1).subplots())
for ax in axs.flat:
    ax.set_axis_off()
for ax in axs[0, :]:
    ax.text(0, .5, "arrowstyle",
            transform=ax.transAxes, size="large", color="tab:blue",
            horizontalalignment="center", verticalalignment="center")
    ax.text(.35, .5, "default parameters",
            transform=ax.transAxes,
            horizontalalignment="left", verticalalignment="center")
```
