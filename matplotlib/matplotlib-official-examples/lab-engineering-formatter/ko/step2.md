# 인공 데이터 생성

플롯할 인공 데이터를 생성해야 합니다. 이 랩에서는 주파수 (Hz) 의 로그를 전력 (Watts) 의 로그에 대해 플롯합니다. `numpy` 라이브러리를 사용하여 데이터를 생성합니다.

```python
# Fixing random state for reproducibility
prng = np.random.RandomState(19680801)

# Create artificial data to plot.
# The x data span over several decades to demonstrate several SI prefixes.
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2
```
