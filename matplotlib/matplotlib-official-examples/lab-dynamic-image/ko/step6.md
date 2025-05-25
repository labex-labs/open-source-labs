# 애니메이션 생성

이제 `ArtistAnimation` 메서드를 사용하여 애니메이션을 생성할 것입니다. figure 객체, `ims` 리스트, 프레임 간 간격 (interval), 그리고 반복 지연 (repeat delay) 을 전달할 것입니다.

```python
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
```
