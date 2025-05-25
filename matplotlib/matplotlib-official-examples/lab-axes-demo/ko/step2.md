# 데이터 생성

이 단계에서는 플롯에 사용할 데이터를 생성합니다. NumPy 의 `convolve` 함수를 사용하여 가우시안 컬러 노이즈를 생성하고 Matplotlib 를 사용하여 플롯합니다.

```python
np.random.seed(19680801)
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt

fig, main_ax = plt.subplots()
main_ax.plot(t, s)
```
