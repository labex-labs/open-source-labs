# X 및 Y 축 모두에 제한 추가

마지막으로, x 축과 y 축 모두에 제한을 추가합니다. x 축 오차 막대에 제한을 추가하기 위해 `xlolims` 및 `xuplims` 매개변수를 사용합니다.

```python
# Plot a series with lower and upper limits in both x & y
# constant x-error with varying y-error
xerr = 0.2
yerr = np.full_like(x, 0.2)
yerr[[3, 6]] = 0.3

# mock up some limits by modifying previous data
xlolims = lolims
xuplims = uplims
lolims = np.zeros_like(x)
uplims = np.zeros_like(x)
lolims[[6]] = True  # only limited at this index
uplims[[3]] = True  # only limited at this index

# do the plotting
ax.errorbar(x, y + 2.1, xerr=xerr, yerr=yerr,
            xlolims=xlolims, xuplims=xuplims,
            uplims=uplims, lolims=lolims,
            marker='o', markersize=8, linestyle='none')
```
