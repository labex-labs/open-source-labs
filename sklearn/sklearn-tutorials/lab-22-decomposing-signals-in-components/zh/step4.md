# 潜在狄利克雷分配（LDA）

#### 用于主题建模的 LDA

潜在狄利克雷分配（LDA）是一种生成式概率模型，用于从文档集合中发现抽象主题。LDA 假设文档是主题的混合，并且单词是由这些主题生成的。可以使用 scikit-learn 中的`LatentDirichletAllocation`类来实现 LDA。

```python
from sklearn.decomposition import LatentDirichletAllocation

# 创建一个 LDA 对象，n_components 为所需的主题数量
lda = LatentDirichletAllocation(n_components=5)

# 将 LDA 模型拟合到文档 - 词项矩阵
lda.fit(document_term_matrix)

# 获取主题 - 词项矩阵和文档 - 主题矩阵
topic_term_matrix = lda.components_
document_topic_matrix = lda.transform(document_term_matrix)
```
