# 눈금 및 격자선에 대한 Zorder 설정

`set_axisbelow()` 메서드 또는 `axes.axisbelow` 매개변수를 사용하여 눈금 및 격자선의 `zorder`를 설정할 수 있습니다.

```python
ax = plt.axes()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
```
