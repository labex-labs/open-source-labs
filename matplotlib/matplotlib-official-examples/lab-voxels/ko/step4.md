# 색상 설정

이제 복셀 플롯의 각 객체에 대한 색상을 설정합니다. 3 단계에서 생성한 부울 배열과 동일한 모양의 빈 배열을 생성한 다음, 각 객체의 위치에 따라 색상을 설정합니다.

```python
colors = np.empty(voxelarray.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'
```
