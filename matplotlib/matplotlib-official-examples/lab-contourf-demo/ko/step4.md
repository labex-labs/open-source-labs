# Colormap 및 Extend 설정

마지막으로, colormap 및 extend 설정을 설정합니다. `with_extremes` 메서드를 사용하여 레벨 범위 아래와 위의 값에 대한 색상을 설정합니다. 또한 네 가지 가능한 `extend` 설정인 `'neither'`, `'both'`, `'min'`, 및 `'max'`를 표시하기 위해 네 개의 서브플롯을 생성합니다.

```python
# Set colormap and extend settings
extends = ["neither", "both", "min", "max"]
cmap = plt.colormaps["winter"].with_extremes(under="magenta", over="yellow")

# Create subplots with different extend settings
fig, axs = plt.subplots(2, 2, layout="constrained")
for ax, extend in zip(axs.flat, extends):
    cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extend, origin=origin)
    fig.colorbar(cs, ax=ax, shrink=0.9)
    ax.set_title("extend = %s" % extend)
    ax.locator_params(nbins=4)

# Show plot
plt.show()
```
