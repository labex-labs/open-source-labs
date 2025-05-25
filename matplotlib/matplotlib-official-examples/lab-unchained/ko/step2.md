# 랜덤 데이터 생성

이 단계에서는 플롯을 생성하는 데 사용할 랜덤 데이터를 생성합니다.

```python
# Generate random data
data = np.random.uniform(0, 1, (64, 75))
X = np.linspace(-1, 1, data.shape[-1])
G = 1.5 * np.exp(-4 * X ** 2)
```
