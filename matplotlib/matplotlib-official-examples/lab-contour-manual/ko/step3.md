# 플롯 생성

다음 단계는 플롯을 생성하는 것입니다. 이는 `ContourSet` 함수를 사용하여 수행할 수 있습니다.

```python
fig, ax = plt.subplots()

# filled=True 를 사용하여 채워진 등고선.
cs = ContourSet(ax, [0, 1, 2], [filled01, filled12], filled=True, cmap=cm.bone)
cbar = fig.colorbar(cs)

# 등고선 (채워지지 않음).
lines = ContourSet(
    ax, [0, 1, 2], [lines0, lines1, lines2], cmap=cm.cool, linewidths=3)
cbar.add_lines(lines)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 4.5),
       title='User-specified contours')
```
