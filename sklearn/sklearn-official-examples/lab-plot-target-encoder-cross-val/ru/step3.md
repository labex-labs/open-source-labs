# Создание синтетического набора данных

В этом лабораторном занятии мы создадим синтетический набор данных с тремя категориальными признаками: информативным признаком со средней мощностью (cardinality), неинформативным признаком со средней мощностью и неинформативным признаком с высокой мощностью. Мы будем использовать класс `KBinsDiscretizer` из библиотеки Scikit-learn для генерации информативного признака. Выполните следующий код для создания синтетического набора данных:

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
