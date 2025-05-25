# 애니메이션 생성

마지막 단계는 애니메이션을 생성하는 것입니다. animation 모듈의 FuncAnimation 함수를 사용하여 이 작업을 수행합니다. 이 함수는 그림 객체, 플롯을 업데이트할 함수, 사용할 프레임 수 등 몇 가지 인수를 받습니다.

```python
def animate(i):
    scat.set_offsets((x[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=50)
```
