# 예제 플롯용 데이터 생성

`~.axes.Axes.ticklabel_format`으로 가능한 다양한 구성을 시연하기 위해 세 개의 플롯에 대한 데이터를 생성합니다.

```python
x = np.arange(0, 1, .01)

# Plot 1
plot1_x = x * 1e5 + 1e10
plot1_y = x * 1e-10 + 1e-5

# Plot 2
plot2_x = x * 1e5
plot2_y = x * 1e-4

# Plot 3
plot3_x = -x * 1e5 - 1e10
plot3_y = -x * 1e-5 - 1e-10
```
