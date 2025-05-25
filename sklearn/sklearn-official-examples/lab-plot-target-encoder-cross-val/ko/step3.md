# 합성 데이터 생성

이 실습에서는 세 가지 범주형 특징을 가진 합성 데이터를 생성합니다. 중간 크기의 정보 특징, 중간 크기의 비정보 특징, 그리고 높은 크기의 비정보 특징이 포함됩니다. Scikit-learn 의 `KBinsDiscretizer` 클래스를 사용하여 정보 특징을 생성합니다. 다음 코드를 실행하여 합성 데이터를 생성합니다.

```python
n_samples = 50_000

rng = np.random.RandomState(42)
y = rng.randn(n_samples)
noise = 0.5 * rng.randn(n_samples)
n_categories = 100

kbins = KBinsDiscretizer(
    n_bins=n_categories, encode="ordinal", strategy="uniform", random_state=rng
)
X_informative = kbins.fit_transform((y + noise).reshape(-1, 1))

permuted_categories = rng.permutation(n_categories)
X_informative = permuted_categories[X_informative.astype(np.int32)]

X_shuffled = rng.permutation(X_informative)

X_near_unique_categories = rng.choice(
    int(0.9 * n_samples), size=n_samples, replace=True
).reshape(-1, 1)

X = pd.DataFrame(
    np.concatenate(
        [X_informative, X_shuffled, X_near_unique_categories],
        axis=1,
    ),
    columns=["informative", "shuffled", "near_unique"],
)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
