# 플롯 생성

이 단계에서는 앞서 생성된 랜덤 데이터를 사용하여 플롯을 생성합니다. 구체적으로, 각 데이터 포인트를 성공 변수에 의해 결정되는 성공 기호, 기술 변수에 의해 결정되는 크기, 이륙 각도 변수에 의해 결정되는 회전, 그리고 추력 변수에 의해 결정되는 색상을 가진 마커로 플롯합니다.

```python
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")
```
