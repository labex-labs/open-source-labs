# 데이터 생성

NumPy 를 사용하여 데이터를 생성합니다. 0 과 5 사이의 균일 분포를 갖는 100 개의 데이터 포인트를 생성합니다. 임계값을 2.5 로 설정하고 부울 표현식을 사용하여 레이블을 생성합니다. 처음 50 개의 데이터 포인트를 학습 데이터로, 나머지를 테스트 데이터로 사용합니다.

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```
