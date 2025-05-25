# 플롯 생성

`matplotlib.pyplot.plot()` 함수를 사용하여 플롯을 생성합니다.

```python
# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')
```
