# カーネル近似のためのニストローム法

ニストローム法は、低ランク近似を使用してカーネルを近似する一般的な手法です。この手法は、カーネルが評価されるデータセットをサブサンプリングします。デフォルトでは、RBF カーネルを使用しますが、任意のカーネル関数または事前計算済みのカーネル行列とともに使用できます。

カーネル近似にニストローム法を使用するには、次の手順に従います。

1. 希望するコンポーネント数（つまり、特徴変換の目標次元数）でニストロームオブジェクトを初期化します。

```python
from sklearn.kernel_approximation import Nystroem

n_components = 100
nystroem = Nystroem(n_components=n_components)
```

2. ニストロームオブジェクトを学習データにフィットさせます。

```python
nystroem.fit(X_train)
```

3. ニストロームオブジェクトを使用して学習データとテストデータを変換します。

```python
X_train_transformed = nystroem.transform(X_train)
X_test_transformed = nystroem.transform(X_test)
```
