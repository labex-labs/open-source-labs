# 마스크 배열 생성

이 단계에서는 세 개의 마스크 배열을 생성합니다. 특정 임계값보다 큰 값, 특정 임계값보다 작은 값, 그리고 두 임계값 사이의 값에 대한 배열입니다.

```python
upper = 0.77
lower = -0.77

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)
```
