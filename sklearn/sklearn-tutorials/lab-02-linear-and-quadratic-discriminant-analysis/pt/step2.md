# Gerar dados sintéticos

Em seguida, geraremos dados sintéticos para demonstrar a diferença entre LDA e QDA. Usaremos a função `make_classification` do scikit-learn para criar duas classes com padrões distintos.

```python
from sklearn.datasets import make_classification

# Gerar dados sintéticos
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=1)
```
