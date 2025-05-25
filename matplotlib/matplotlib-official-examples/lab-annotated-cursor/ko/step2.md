# 플롯 생성

NumPy 의 `linspace` 함수를 사용하여 x 에 대해 -5 와 5 사이의 1000 개의 값을 생성한 다음, y 를 x 의 제곱으로 계산하여 포물선의 간단한 플롯을 생성합니다.

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x**2

line, = ax.plot(x, y)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
```
