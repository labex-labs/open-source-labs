# 극좌표 플롯 생성

이제 `matplotlib.pyplot`의 `polar` 함수를 사용하여 극좌표 플롯을 생성합니다.

```python
ax = plt.subplot(2, 1, 2, projection='polar')

# Plot the data
for x, y in zip(xs, ys):
    plt.polar(x, y, 'ro')
```
