# 선 그래프를 위한 데이터 생성

이 단계에서는 선 그래프를 위한 데이터를 생성합니다. NumPy 의 `linspace` 함수를 사용하여 0 과 10 사이의 균등하게 간격이 띄워진 값의 배열을 생성합니다. 또한 NumPy 의 `random.randn` 함수를 사용하여 일부 임의 노이즈 (random noise) 를 생성합니다.

```python
x = np.linspace(0, 10)
np.random.seed(19680801)
noise = np.random.randn(50)
```
