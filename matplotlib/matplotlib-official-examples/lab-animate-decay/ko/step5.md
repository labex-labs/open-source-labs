# 애니메이션 함수 정의

이제 애니메이션의 각 프레임에 대해 플롯을 업데이트하는 함수를 정의해야 합니다. 이 함수는 `data_gen()` 함수에서 생성된 데이터를 가져와 새 데이터로 플롯을 업데이트합니다. 또한 애니메이션이 진행됨에 따라 x 축 제한을 업데이트합니다.

```python
def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,
```
