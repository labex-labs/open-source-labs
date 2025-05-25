# 최적 적합선 추가

이 단계에서는 히스토그램에 최적 적합선을 추가합니다. 선의 y 값을 계산하고 히스토그램 위에 플롯합니다.

```python
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
```
