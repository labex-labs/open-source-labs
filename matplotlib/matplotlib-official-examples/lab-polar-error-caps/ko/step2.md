# 데이터 생성

이 단계에서는 오차 막대 플롯에 사용할 데이터를 생성합니다. NumPy 를 사용하여 세타 (theta) 값의 배열과 해당 반경 (radius) 값의 배열을 생성합니다.

```python
theta = np.arange(0, 2 * np.pi, np.pi / 4)
r = theta / np.pi / 2 + 0.5
```
