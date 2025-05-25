# 신호 생성

NumPy 를 사용하여 신호를 생성합니다. linspace 함수를 사용하여 xdata 배열을 생성하며, start=16, stop=365, num=(365-16)\*4 로 설정합니다. sin 및 cos 함수를 사용하여 ydata 배열을 생성합니다.

```python
xdata = np.linspace(16, 365, (365-16)*4)
ydata = np.sin(2*np.pi*xdata/153) + np.cos(2*np.pi*xdata/127)
```
