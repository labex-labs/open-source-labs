# 큐브 생성 및 연결

이제 두 개의 큐브와 그 사이의 연결을 생성합니다. 세 개의 부울 배열을 정의하여 이를 수행하고, 이를 단일 부울 배열로 결합합니다. 처음 두 배열은 큐브의 위치를 정의하고, 세 번째 배열은 연결의 위치를 정의합니다.

```python
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

voxelarray = cube1 | cube2 | link
```
