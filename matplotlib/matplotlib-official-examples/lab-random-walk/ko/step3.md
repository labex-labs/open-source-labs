# 업데이트 함수 정의

애니메이션의 각 프레임에 대해 플롯을 업데이트하는 함수를 정의합니다. 이 함수는 세 개의 입력을 받습니다: `num`은 현재 프레임 번호이고, `walks`는 모든 랜덤 워크의 목록이며, `lines`는 플롯의 모든 선의 목록입니다. 각 선과 워크에 대해, 현재 프레임 번호까지 선의 x, y, z 좌표에 대한 데이터를 업데이트합니다. `line.set_data()`와 `line.set_3d_properties()`를 사용하여 각각 x-y 및 z 좌표를 업데이트합니다.

```python
def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines
```
