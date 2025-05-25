# 내부 그리드 및 서브플롯 생성

이 단계에서는 중첩된 `.GridSpec`을 사용하여 내부 그리드와 서브플롯을 생성합니다. 외부 그리드의 각 셀을 반복하고 각 셀에 대해 3x3 그리드를 생성합니다.

```python
for a in range(4):
    for b in range(4):
        # gridspec inside gridspec
        inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
        axs = inner_grid.subplots()  # Create all subplots for the inner grid.
        for (c, d), ax in np.ndenumerate(axs):
            ax.plot(*squiggle_xy(a + 1, b + 1, c + 1, d + 1))
            ax.set(xticks=[], yticks=[])
```
