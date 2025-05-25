# 애니메이션 객체 생성

이제 `FuncAnimation()` 함수를 사용하여 애니메이션 객체를 생성할 수 있습니다. figure 객체, 애니메이션 함수, 업데이트 간격 및 저장할 프레임 수를 전달합니다.

```python
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
```
