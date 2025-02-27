# Asignación Latente de Dirichlet (LDA)

#### LDA para modelado de temas

La Asignación Latente de Dirichlet (LDA, por sus siglas en inglés) es un modelo probabilístico generativo utilizado para descubrir temas abstractos a partir de una colección de documentos. La LDA asume que los documentos son una mezcla de temas y que las palabras son generadas por estos temas. La LDA se puede implementar utilizando la clase `LatentDirichletAllocation` de scikit-learn.

```python
from sklearn.decomposition import LatentDirichletAllocation

# Crea un objeto LDA con n_components como el número de temas deseados
lda = LatentDirichletAllocation(n_components=5)

# Ajusta el modelo LDA a la matriz documento-término
lda.fit(document_term_matrix)

# Obtiene la matriz tema-término y la matriz documento-tema
topic_term_matrix = lda.components_
document_topic_matrix = lda.transform(document_term_matrix)
```
