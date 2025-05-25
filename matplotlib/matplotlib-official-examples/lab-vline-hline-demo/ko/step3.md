# 데이터에 노이즈 추가

이 단계에서는 데이터를 더 현실적으로 만들기 위해 약간의 노이즈를 추가합니다. NumPy 의 `normal` 함수를 사용하여 평균 0.0 과 표준 편차 0.3 을 갖는 난수를 생성합니다.

```python
# Add noise to the data
nse = np.random.normal(0.0, 0.3, t.shape) * s
```
