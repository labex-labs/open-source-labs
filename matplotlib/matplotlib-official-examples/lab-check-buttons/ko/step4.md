# 체크 버튼 추가

이제 `CheckButtons` 함수를 사용하여 플롯에 체크 버튼을 추가합니다. 플롯된 선을 레이블로 전달하고 각 선의 초기 가시성을 설정합니다. 또한 플롯된 선의 색상과 일치하도록 체크 버튼의 속성을 조정합니다.

```python
lines_by_label = {l.get_label(): l for l in [l0, l1, l2]}
line_colors = [l.get_color() for l in lines_by_label.values()]

rax = fig.add_axes([0.05, 0.4, 0.1, 0.15])
check = CheckButtons(
    ax=rax,
    labels=lines_by_label.keys(),
    actives=[l.get_visible() for l in lines_by_label.values()],
    label_props={'color': line_colors},
    frame_props={'edgecolor': line_colors},
    check_props={'facecolor': line_colors},
)
```
