# 간단한 선 그래프 만들기

이 단계에서는 Matplotlib 를 사용하여 간단한 선 그래프를 만들 것입니다. 먼저 NumPy 의 `linspace()` 함수와 `cos()` 함수를 사용하여 플롯할 데이터를 생성합니다. 그런 다음 `plot()` 함수를 사용하여 그래프를 만듭니다.

```python
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.show()
```
