# 애니메이션 생성

일곱 번째 단계는 `FuncAnimation` 함수를 사용하여 애니메이션 객체를 생성하는 것입니다. 우리는 figure 객체, 애니메이션 함수, 프레임 간 간격 (interval, 밀리초 단위), 프레임 수, 그리고 애니메이션을 반복하기 전의 지연 시간을 전달합니다.

```python
ani = animation.FuncAnimation(
    fig,
    animate,
    interval=50,
    blit=False,  # blitting can't be used with Figure artists
    frames=x,
    repeat_delay=100,
)
```
