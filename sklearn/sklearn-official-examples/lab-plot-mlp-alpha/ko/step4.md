# 데이터셋 생성

`make_classification`, `make_moons`, 그리고 `make_circles` 함수를 사용하여 scikit-learn 에서 세 가지 합성 데이터셋을 생성합니다. 각 데이터셋을 학습용과 테스트용으로 분할합니다.

```python
X, y = make_classification(
    n_features=2, n_redundant=0, n_informative=2, random_state=0, n_clusters_per_class=1
)
rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)
linearly_separable = (X, y)

datasets = [
    make_moons(noise=0.3, random_state=0),
    make_circles(noise=0.2, factor=0.5, random_state=1),
    linearly_separable,
]

figure = plt.figure(figsize=(17, 9))
i = 1
# 데이터셋 반복
for X, y in datasets:
    # 학습 및 테스트 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42
    )
```
