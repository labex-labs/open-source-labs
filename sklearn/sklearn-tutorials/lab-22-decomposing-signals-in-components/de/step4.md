# Latent Dirichlet Allokation (LDA)

#### LDA für die Themensuche

Die Latent Dirichlet Allokation (LDA) ist ein generatives probabilistisches Modell, das zur Entdeckung abstrakter Themen aus einer Sammlung von Dokumenten verwendet wird. Die LDA geht davon aus, dass Dokumente eine Mischung von Themen sind und dass Wörter von diesen Themen generiert werden. Die LDA kann mit der Klasse `LatentDirichletAllocation` aus scikit-learn implementiert werden.

```python
from sklearn.decomposition import LatentDirichletAllocation

# Erstellen eines LDA-Objekts mit n_components als Anzahl der gewünschten Themen
lda = LatentDirichletAllocation(n_components=5)

# Anpassen des LDA-Modells an die Dokument-Term-Matrix
lda.fit(document_term_matrix)

# Abrufen der Thema-Term-Matrix und der Dokument-Thema-Matrix
topic_term_matrix = lda.components_
document_topic_matrix = lda.transform(document_term_matrix)
```
