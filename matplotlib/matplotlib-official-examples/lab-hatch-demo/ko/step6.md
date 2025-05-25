# 해칭을 사용한 타원 패치 (Ellipse Patch) 추가

플롯에 해칭된 패치를 추가할 수도 있습니다. 이 경우, `add_patch` 함수를 사용하여 플롯에 타원 패치를 추가합니다.

```python
plt.gca().add_patch(Ellipse((4, 50), 10, 10, fill=True, hatch='*', facecolor='y'))
```
