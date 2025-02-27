# テンソルスケッチを用た多項式カーネル近似

多項式カーネルは、特徴間の相互作用をモデル化する人気のあるカーネル関数です。PolynomialCountSketch クラスは、テンソルスケッチアプローチを使ってこのカーネルを近似するための拡張可能な方法を提供します。

カーネル近似に PolynomialCountSketch を使用するには、次の手順に従います。

1. 希望する次数 (d) とコンポーネント数で PolynomialCountSketch オブジェクトを初期化します。

```python
from sklearn.kernel_approximation import PolynomialCountSketch

degree = 3
n_components = 100
polynomial_count_sketch = PolynomialCountSketch(degree=degree, n_components=n_components)
```

2. PolynomialCountSketch オブジェクトを学習データにフィットさせます。

```python
polynomial_count_sketch.fit(X_train)
```

3. PolynomialCountSketch オブジェクトを使用して学習データとテストデータを変換します。

```python
X_train_transformed = polynomial_count_sketch.transform(X_train)
X_test_transformed = polynomial_count_sketch.transform(X_test)
```
