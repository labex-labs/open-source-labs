# 데이터 로드 및 분할

make_hastie_10_2 데이터셋을 사용하여 학습 데이터와 테스트 데이터로 분할합니다.

```python
X, y = datasets.make_hastie_10_2(n_samples=4000, random_state=1)

# 레이블을 {-1, 1}에서 {0, 1}로 매핑
labels, y = np.unique(y, return_inverse=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)
```
