# 프레임 획득 및 파일에 쓰기

100 번의 반복을 통해 x 및 y 좌표에 대한 난수를 생성합니다. 선 플롯의 데이터를 업데이트하고 writer 를 사용하여 프레임을 획득합니다. 마지막으로, 프레임을 파일에 저장합니다.

```python
x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()
```
