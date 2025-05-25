# 플롯할 데이터 평가

이제 플롯할 데이터를 평가합니다. 이 예제에서는 목적 함수 (`objective function`) `g1`, `g2`, `g3`를 플롯합니다.

```python
# Evaluate some stuff to plot
obj = x1**2 + x2**2 - 2*x1 - 2*x2 + 2
g1 = -(3*x1 + x2 - 5.5)
g2 = -(x1 + 2*x2 - 4.5)
g3 = 0.8 + x1**-3 - x2
```
