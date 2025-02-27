# 主成分分析 (PCA)

#### 正確な PCA と確率的解釈

主成分分析 (Principal Component Analysis: PCA) は、多変量データセットを、最大限の分散を説明する一連の直交コンポーネントに分解するために使用されます。PCA は、scikit-learn の `PCA` クラスを使用して実装できます。`fit` メソッドはコンポーネントを学習するために使用され、`transform` メソッドは新しいデータをこれらのコンポーネントに射影するために使用できます。

```python
from sklearn.decomposition import PCA

# 目的のコンポーネント数を n_components として PCA オブジェクトを作成
pca = PCA(n_components=2)

# PCA モデルをデータに適合させる
pca.fit(data)

# 学習したコンポーネントにデータを射影することでデータを変換する
transformed_data = pca.transform(data)
```
