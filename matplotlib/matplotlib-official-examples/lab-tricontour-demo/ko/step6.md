# 색상 없이 라벨링된 해칭 패턴 생성

`ax.tricontourf`에서 `colors` 매개변수를 `"none"`으로 지정하여 색상 없이 라벨링된 해칭 패턴을 생성할 수 있습니다. 또한 `ContourSet.legend_elements`를 사용하여 등고선 세트에 대한 범례를 만들 수 있습니다.

```python
fig3, ax3 = plt.subplots()
n_levels = 7
tcf = ax3.tricontourf(
    triang,
    z,
    n_levels,
    colors="none",
    hatches=[".", "/", "\\", None, "\\\\", "*"],
)
ax3.tricontour(triang, z, n_levels, colors="black", linestyles="-")

artists, labels = tcf.legend_elements(str_format="{:2.1f}".format)
ax3.legend(artists, labels, handleheight=2, framealpha=1)
```
