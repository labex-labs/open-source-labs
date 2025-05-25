# 데이터 생성

다음으로, 샘플 데이터를 생성합니다. 이 랩에서는 2 차원 사인파를 생성합니다.

```python
t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
```
