# リッチなHTML表現

推定器を表示する2番目の方法は、リッチなHTML表現を通じるものです。ノートブックでは、推定器とパイプラインはリッチなHTML表現を使用します。これは、パイプラインやその他の複合推定器の構造を要約し、詳細を提供するためのインタラクティビティ付きで特に便利です。

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# 数値型とカテゴリ型のデータ用のパイプラインを作成する
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)

# 特定の列に数値型とカテゴリ型のパイプラインを適用する前処理機を作成する
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)

# 前処理機とロジスティック回帰を適用するパイプラインを作成する
clf = make_pipeline(preprocessor, LogisticRegression())

# パイプラインを表示する
clf
```
