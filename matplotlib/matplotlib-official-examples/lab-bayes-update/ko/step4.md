# 애니메이션 생성

이제 `UpdateDist` 클래스를 정의했으므로 Matplotlib 의 `FuncAnimation` 클래스를 사용하여 애니메이션을 생성할 수 있습니다. figure 객체와 axis 객체를 생성하고 axis 객체를 `UpdateDist` 클래스에 전달하여 클래스의 새 인스턴스를 생성합니다.

```python
fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=100, interval=100, blit=True)
plt.show()
```

`FuncAnimation` 클래스는 여러 인수를 받습니다:

- `fig`: figure 객체
- `ud`: `UpdateDist` 인스턴스
- `frames`: 애니메이션할 프레임 수
- `interval`: 프레임 간의 시간 간격 (밀리초)
- `blit`: 변경된 플롯의 부분만 업데이트할지 여부
