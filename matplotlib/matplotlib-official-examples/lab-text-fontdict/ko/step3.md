# 플롯 생성

이제 플롯을 생성할 수 있습니다. NumPy 를 사용하여 데이터를 생성하고 감쇠 지수 감소 곡선을 플롯합니다.

```python
x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

plt.plot(x, y, 'k')
```
