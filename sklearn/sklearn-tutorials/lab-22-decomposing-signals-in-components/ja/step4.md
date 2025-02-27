# 潜在的ディリクレ配分 (LDA)

#### トピックモデリングのための LDA

潜在的ディリクレ配分 (Latent Dirichlet Allocation: LDA) は、文書のコレクションから抽象的なトピックを発見するために使用される生成確率モデルです。LDA は、文書がトピックの混合物であり、単語がこれらのトピックによって生成されると仮定しています。LDA は、scikit - learn の `LatentDirichletAllocation` クラスを使用して実装できます。

```python
from sklearn.decomposition import LatentDirichletAllocation

# 目的のトピック数を n_components として LDA オブジェクトを作成
lda = LatentDirichletAllocation(n_components=5)

# LDA モデルを文書 - 用語行列に適合させる
lda.fit(document_term_matrix)

# トピック - 用語行列と文書 - トピック行列を取得する
topic_term_matrix = lda.components_
document_topic_matrix = lda.transform(document_term_matrix)
```
