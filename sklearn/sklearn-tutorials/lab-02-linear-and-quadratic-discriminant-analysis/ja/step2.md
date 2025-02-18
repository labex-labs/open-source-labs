# 合成データを生成する

次に、LDA と QDA の違いを示すために合成データを生成します。scikit-learn の `make_classification` 関数を使用して、異なるパターンを持つ2つのクラスを作成します。

```python
from sklearn.datasets import make_classification

# Generate synthetic data
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=1)
```
