# 타이머 객체 생성

새로운 타이머 객체를 생성합니다. 간격 (interval) 을 100 밀리초 (기본값은 1000) 로 설정하고 타이머에게 어떤 함수를 호출해야 하는지 알려줍니다.

```python
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update_title, ax)
```
