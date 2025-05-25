# 데이터 섞기

분석의 무작위성을 보장하기 위해 데이터 세트의 샘플 순서를 섞어 보겠습니다.

```python
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]
```
