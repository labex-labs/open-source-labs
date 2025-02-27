# 非負行列分解 (NMF)

#### フロベニウスノルムを用いた NMF

非負行列分解 (Non - negative Matrix Factorization: NMF) は、非負のデータとコンポーネントを仮定する分解のための代替アプローチです。データと 2 つの行列の行列積の間の距離を最適化することにより、非負の要素からなる 2 つの行列にデータを分解します。NMF は、scikit - learn の `NMF` クラスを使用して実装できます。

```python
from sklearn.decomposition import NMF

# 目的のコンポーネント数を n_components として NMF オブジェクトを作成
nmf = NMF(n_components=2)

# NMF モデルをデータに適合させる
nmf.fit(data)

# データを 2 つの非負行列に分解する
matrix_W = nmf.transform(data)
matrix_H = nmf.components_
```
