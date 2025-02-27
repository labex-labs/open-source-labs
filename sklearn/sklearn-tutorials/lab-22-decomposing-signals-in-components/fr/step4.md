# Allocation Latente de Dirichlet (LDA)

#### LDA pour la modélisation de sujets

L'Allocation Latente de Dirichlet (LDA) est un modèle probabiliste génératif utilisé pour découvrir des sujets abstraits à partir d'un ensemble de documents. LDA suppose que les documents sont un mélange de sujets et que les mots sont générés par ces sujets. LDA peut être implémentée à l'aide de la classe `LatentDirichletAllocation` de scikit-learn.

```python
from sklearn.decomposition import LatentDirichletAllocation

# Crée un objet LDA avec n_components comme nombre de sujets souhaités
lda = LatentDirichletAllocation(n_components=5)

# Ajuste le modèle LDA à la matrice document-terme
lda.fit(document_term_matrix)

# Obtiens la matrice sujet-terme et la matrice document-sujet
topic_term_matrix = lda.components_
document_topic_matrix = lda.transform(document_term_matrix)
```
