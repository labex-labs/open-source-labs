# 플롯 형식 지정

플롯의 가독성을 높이기 위해 Matplotlib 의 형식 지정 함수를 사용하여 형식을 지정할 수 있습니다. 이 예제에서는 y 축 레이블이 백만 단위로 값을 표시하도록 형식을 지정합니다.

```python
def millions(x):
    return '$%1.1fM' % (x * 1e-6)

ax.fmt_ydata = millions
```
