# 데이터 생성

이 단계에서는 오차 막대 플롯을 생성하는 데 사용할 데이터를 생성합니다.

```python
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)
```
