# 데이터 플롯

이 단계에서는 Matplotlib 의 `plot` 함수를 사용하여 axes 객체에 데이터를 플롯합니다. 서로 다른 기울기와 임의 노이즈를 가진 여섯 개의 서로 다른 선을 플롯합니다.

```python
ax.plot(x, np.sin(x) + x + noise)
ax.plot(x, np.sin(x) + 0.5 * x + noise)
ax.plot(x, np.sin(x) + 2 * x + noise)
ax.plot(x, np.sin(x) - 0.5 * x + noise)
ax.plot(x, np.sin(x) - 2 * x + noise)
ax.plot(x, np.sin(x) + noise)
```
