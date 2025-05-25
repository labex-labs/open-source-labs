# Spines 오프셋

`set_position()` 함수를 사용하여 왼쪽 및 아래쪽 spines 를 바깥쪽으로 10 포인트 이동합니다. `set_position()`의 인수는 두 개의 요소가 있는 튜플입니다. 첫 번째 요소는 spine 의 위치를 나타내고, 두 번째 요소는 spine 에서 플롯 영역까지의 거리를 나타냅니다.

```python
ax.spines[['left', 'bottom']].set_position(('outward', 10))
```
