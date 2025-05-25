# 산점도 생성

이제 `matplotlib.pyplot`의 `plot` 함수를 사용하여 산점도를 생성합니다.

```python
fig = plt.figure(figsize=(5, 10))
ax = plt.subplot(2, 1, 1)

# Plot the data
for x, y in zip(xs, ys):
    plt.plot(x, y, 'ro')
```
