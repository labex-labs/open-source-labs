# 삽입 위치 및 크기 제어

`bbox_to_anchor` 및 `bbox_transform` 매개변수를 사용하여 삽입의 위치와 크기를 제어할 수 있습니다. 이러한 매개변수를 사용하면 삽입 위치와 크기를 세밀하게 제어하거나, 삽입을 완전히 임의의 위치에 배치할 수도 있습니다.

```python
# bbox_transform 으로 축 변환을 사용합니다. 따라서 경계 상자는
# 축 좌표로 지정해야 합니다 ((0, 0) 은 축의 왼쪽 하단 모서리이고, (1, 1) 은 오른쪽 상단 모서리입니다).
# 경계 상자 (.2, .4, .6, .5) 는 (.2, .4) 에서 시작하여 해당 좌표에서 (.8, .9) 까지 범위가 지정됩니다.
# 이 경계 상자 내에서 경계 상자 너비의 절반과
# 경계 상자 높이의 3/4 인 삽입이 생성됩니다. 삽입의 왼쪽 하단 모서리는 경계 상자의 왼쪽 하단 모서리에 맞춰집니다 (loc=3).
# 그런 다음 삽입은 글꼴 크기 단위로 기본 0.5 만큼 오프셋됩니다.
axins = inset_axes(ax, width="50%", height="75%",
                   bbox_to_anchor=(.2, .4, .6, .5),
                   bbox_transform=ax.transAxes, loc=3)
```
