# 加算チカ二乗 (ACS) カーネル近似

ACS カーネルは、ヒストグラム上のカーネルであり、コンピュータビジョンで一般的に使用されます。AdditiveChi2Sampler クラスは、このカーネルの近似マッピングを提供します。

カーネル近似に AdditiveChi2Sampler を使用するには、次の手順に従います。

1. 希望するサンプル数 (n) と正則化パラメータ (c) で AdditiveChi2Sampler オブジェクトを初期化します。

```python
from sklearn.kernel_approximation import AdditiveChi2Sampler

n_samples = 1000
c = 1.0
additive_chi2_sampler = AdditiveChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=2, c=c)
```

2. AdditiveChi2Sampler オブジェクトを学習データにフィットさせます。

```python
additive_chi2_sampler.fit(X_train)
```

3. AdditiveChi2Sampler オブジェクトを使用して学習データとテストデータを変換します。

```python
X_train_transformed = additive_chi2_sampler.transform(X_train)
X_test_transformed = additive_chi2_sampler.transform(X_test)
```
