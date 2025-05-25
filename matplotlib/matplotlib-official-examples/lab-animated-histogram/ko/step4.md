# 애니메이션 함수 생성

새로운 랜덤 데이터를 생성하고 사각형의 높이를 업데이트하는 `animate` 함수를 생성해야 합니다.

```python
def animate(frame_number):
    # simulate new data coming in
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)
    return bar_container.patches
```
