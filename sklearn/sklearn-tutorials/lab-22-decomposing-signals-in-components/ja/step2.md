# 独立成分分析 (ICA)

#### ブラインドソース分離のための ICA

独立成分分析 (Independent Component Analysis: ICA) は、混合された信号を元のソースコンポーネントに分離するために使用されます。ICA は、コンポーネントが統計的に独立であり、線形なアンミキシング処理によって抽出できると仮定しています。ICA は、scikit-learn の `FastICA` クラスを使用して実装できます。

```python
from sklearn.decomposition import FastICA

# 目的のコンポーネント数を n_components として ICA オブジェクトを作成
ica = FastICA(n_components=2)

# ICA モデルを混合信号に適合させる
ica.fit(mixed_signals)

# 混合信号を元のソースコンポーネントに分離する
source_components = ica.transform(mixed_signals)
```
