# 플롯 생성

다음으로, Matplotlib 을 사용하여 플롯을 생성합니다. 이 예제에서는 코사인 함수를 값의 범위에 걸쳐 플롯합니다.

```python
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
```
