# 신뢰 구간 (Confidence Bands)

`fill_between`의 일반적인 응용 분야는 신뢰 구간 표시입니다. `fill_between`은 채우기 색상으로 색상 순환 (color cycle) 의 색상을 사용합니다. 따라서 *alpha*를 사용하여 영역을 반투명하게 만들어 색상을 밝게 하는 것이 좋은 방법입니다.

```python
N = 21
x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# fit a linear curve and estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')
```
