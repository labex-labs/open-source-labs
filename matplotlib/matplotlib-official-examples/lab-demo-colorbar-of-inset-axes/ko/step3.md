# 삽입 축 생성

`zoomed_inset_axes` 함수를 사용하여 삽입 축 (inset axis) 을 생성합니다. 메인 플롯 내에서 삽입 축의 확대 수준 (zoom level) 과 위치를 설정합니다.

```python
axins = zoomed_inset_axes(ax, zoom=2, loc='upper left')
axins.set(xticks=[], yticks=[])
```
