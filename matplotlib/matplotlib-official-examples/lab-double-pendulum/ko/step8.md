# 애니메이션 생성

이제 Matplotlib 의 `FuncAnimation` 함수를 사용하여 애니메이션을 생성합니다.

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```
