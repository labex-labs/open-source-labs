# 데이터 생성

다음으로, 상자 그림에 사용할 샘플 데이터를 생성합니다. 이 튜토리얼에서는 다음 데이터를 사용합니다.

```python
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
```
