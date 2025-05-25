# 대각선 그리기

먼저, Matplotlib 의 `plot()` 함수를 사용하여 45 도 각도의 대각선을 그립니다.

```python
fig, ax = plt.subplots()

# Plot diagonal line (45 degrees)
h = ax.plot(range(0, 10), range(0, 10))
```
