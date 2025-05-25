# 박스 플롯을 사용자 정의 색상으로 채우기

다음으로, 박스 플롯을 사용자 정의 색상으로 채웁니다. 색상 목록을 생성하고 루프를 사용하여 각 상자를 다른 색상으로 채웁니다.

```python
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
```
