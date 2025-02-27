# Erstellen eines synthetischen Datensatzes

Für dieses Lab werden wir einen synthetischen Datensatz mit drei kategorischen Features erstellen: ein informatives Feature mit mittlerer Kardinalität, ein uninformatives Feature mit mittlerer Kardinalität und ein uninformatives Feature mit hoher Kardinalität. Wir werden die `KBinsDiscretizer`-Klasse aus Scikit-learn verwenden, um das informative Feature zu generieren. Führen Sie den folgenden Code aus, um den synthetischen Datensatz zu erstellen:

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