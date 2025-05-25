# 해칭된 패치 (Patch) 를 사용한 플롯 생성

플롯에서 패치와 함께 해칭을 사용할 수도 있습니다. 이 경우, `fill_between` 함수를 사용하여 해칭된 패치를 생성합니다.

```python
x = np.arange(0, 40, 0.2)
plt.fill_between(x, np.sin(x) * 4 + 30, y2=0, hatch='///', zorder=2, fc='c')
```
