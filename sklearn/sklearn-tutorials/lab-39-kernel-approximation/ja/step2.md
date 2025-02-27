# ラジアルベーシス関数 (RBF) カーネル近似

RBFSampler クラスは、ランダムキッチンシンクとしても知られる RBF カーネルの近似マッピングを実装しています。この手法を使うことで、線形 SVM やロジスティック回帰などの線形アルゴリズムを適用する前に、カーネルマップを明示的にモデル化することができます。

カーネル近似に RBFSampler を使うには、次の手順に従います。

1. ガンマ（RBF カーネルのパラメータ）の希望値とコンポーネント数で RBFSampler オブジェクトを初期化します。

```python
from sklearn.kernel_approximation import RBFSampler

gamma = 0.1
n_components = 100
rbf_sampler = RBFSampler(gamma=gamma, n_components=n_components)
```

2. RBFSampler オブジェクトを学習データにフィットさせます。

```python
rbf_sampler.fit(X_train)
```

3. RBFSampler オブジェクトを使って学習データとテストデータを変換します。

```python
X_train_transformed = rbf_sampler.transform(X_train)
X_test_transformed = rbf_sampler.transform(X_test)
```
