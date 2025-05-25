# 해칭을 사용한 다각형 패치 (Polygon Patch) 추가

해칭을 사용한 다각형 패치도 추가할 수 있습니다. 이 경우, `add_patch` 함수를 사용하여 플롯에 다각형 패치를 추가합니다.

```python
plt.gca().add_patch(Polygon([(10, 20), (30, 50), (50, 10)], hatch='\\/...', facecolor='g'))
```
