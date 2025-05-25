# 데이터 로드 및 셔플

먼저 숫자 데이터셋을 로드하고 데이터를 무작위로 섞습니다.

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```
