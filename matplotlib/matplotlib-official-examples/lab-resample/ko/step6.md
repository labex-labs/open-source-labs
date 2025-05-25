# 플롯 생성

Matplotlib 를 사용하여 플롯을 생성합니다. xdata 와 ydata 를 사용하여 `DataDisplayDownsampler` 클래스의 인스턴스 `d`를 생성합니다. subplots 함수를 사용하여 figure 와 axis 를 생성합니다. 선을 연결하고 autoscale 을 False 로 설정합니다. 뷰 제한 변경에 연결하고, x 제한을 설정한 다음 플롯을 표시합니다.

```python
d = DataDisplayDownsampler(xdata, ydata)
fig, ax = plt.subplots()
d.line, = ax.plot(xdata, ydata, 'o-')
ax.set_autoscale_on(False)
ax.callbacks.connect('xlim_changed', d.update)
ax.set_xlim(16, 365)
plt.show()
```
