# Alocação Dirichlet Latente (LDA)

#### LDA para modelagem de tópicos

A Alocação Dirichlet Latente (LDA) é um modelo probabilístico gerativo usado para descobrir tópicos abstratos a partir de uma coleção de documentos. A LDA assume que os documentos são uma mistura de tópicos e que as palavras são geradas por esses tópicos. A LDA pode ser implementada usando a classe `LatentDirichletAllocation` do scikit-learn.

```python
from sklearn.decomposition import LatentDirichletAllocation

# Crie um objeto LDA com n_components como o número de tópicos desejados
lda = LatentDirichletAllocation(n_components=5)

# Ajuste o modelo LDA à matriz documento-termo
lda.fit(document_term_matrix)

# Obtenha a matriz tópico-termo e a matriz documento-tópico
topic_term_matrix = lda.components_
document_topic_matrix = lda.transform(document_term_matrix)
```
