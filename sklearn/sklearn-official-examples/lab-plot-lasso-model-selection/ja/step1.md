# データセット

まず、`sklearn.datasets` からの `load_diabetes` 関数を使用して糖尿病データセットを読み込みます。このデータセットは、10のベースライン変数、年齢、性別、体重指数、平均血圧、および6つの血清測定値と、ベースラインから1年後の病気進行の定量的測定値で構成されています。

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
X.head()
```
