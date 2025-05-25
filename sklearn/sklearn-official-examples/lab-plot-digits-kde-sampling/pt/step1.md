# Carregar Dados

Primeiro, carregamos o conjunto de dados de dígitos do scikit-learn. Este conjunto de dados contém imagens de 8x8 de dígitos de 0 a 9. Usaremos Análise de Componentes Principais (PCA) para reduzir a dimensão do conjunto de dados para 15.

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# carregar o conjunto de dados de dígitos
digits = load_digits()

# reduzir a dimensão do conjunto de dados para 15 usando PCA
pca = PCA(n_components=15, whiten=False)
data = pca.fit_transform(digits.data)
```
