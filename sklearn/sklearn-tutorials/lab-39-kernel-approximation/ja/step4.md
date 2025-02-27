# 歪チカ二乗 (SCS) カーネル近似

SCS カーネルは、特徴マップの単純なモンテカルロ近似を可能にする指数化チカ二乗カーネルのバリアントです。SkewedChi2Sampler クラスは、このカーネルの近似マッピングを提供します。

カーネル近似に SkewedChi2Sampler を使用するには、次の手順に従います。

1. 希望するサンプル数 (n) と正則化パラメータ (c) で SkewedChi2Sampler オブジェクトを初期化します。

```python
from sklearn.kernel_approximation import SkewedChi2Sampler

n_samples = 1000
c = 1.0
skewed_chi2_sampler = SkewedChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=1, c=c)
```

2. SkewedChi2Sampler オブジェクトを学習データにフィットさせます。

```python
skewed_chi2_sampler.fit(X_train)
```

3. SkewedChi2Sampler オブジェクトを使用して学習データとテストデータを変換します。

```python
X_train_transformed = skewed_chi2_sampler.transform(X_train)
X_test_transformed = skewed_chi2_sampler.transform(X_test)
```
