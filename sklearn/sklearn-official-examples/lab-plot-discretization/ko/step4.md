# 입력 특징 이산화

이 단계에서는 `KBinsDiscretizer` 클래스를 사용하여 입력 특징을 이산화합니다. 10 개의 구간을 생성하고 원 - 핫 인코딩을 사용하여 데이터를 변환합니다.

```python
enc = KBinsDiscretizer(n_bins=10, encode="onehot")
X_binned = enc.fit_transform(X)
```
