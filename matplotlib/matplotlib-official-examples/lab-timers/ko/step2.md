# 제목 업데이트 함수 정의

현재 시간으로 그림의 제목을 업데이트하는 함수를 정의합니다.

```python
def update_title(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()
```
