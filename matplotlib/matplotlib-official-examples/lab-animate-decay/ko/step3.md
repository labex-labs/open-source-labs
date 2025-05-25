# 플롯 설정

이제 플롯을 설정해야 합니다. Matplotlib 의 `subplots()` 함수를 사용하여 figure 와 axes 객체를 생성합니다. 또한 사인파를 나타내는 line 객체를 생성합니다.

```python
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
```
