# Латентное Дирихлево распределение (LDA)

#### LDA для моделирования тем

Латентное Дирихлево распределение (LDA) - это генеративная вероятностная модель, используемая для обнаружения абстрактных тем из коллекции документов. LDA предполагает, что документы представляют собой смесь тем, а слова генерируются этими темами. LDA можно реализовать с использованием класса `LatentDirichletAllocation` из scikit-learn.

```python
from sklearn.decomposition import LatentDirichletAllocation

# Создайте объект LDA с n_components в качестве количества желаемых тем
lda = LatentDirichletAllocation(n_components=5)

# Подгоньте модель LDA к матрице документ - терм
lda.fit(document_term_matrix)

# Получите матрицу тем - терм и матрицу документ - темы
topic_term_matrix = lda.components_
document_topic_matrix = lda.transform(document_term_matrix)
```
