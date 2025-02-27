# 合成データセットの作成

この実験では、3 つのカテゴリ特徴量を持つ合成データセットを作成します。具体的には、中程度のカーディナリティを持つ有益な特徴量、中程度のカーディナリティを持つ無益な特徴量、および高いカーディナリティを持つ無益な特徴量です。有益な特徴量の生成には、Scikit-learn の `KBinsDiscretizer` クラスを使用します。以下のコードを実行して、合成データセットを作成してください。

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
