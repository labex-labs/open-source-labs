# Gerar Conjunto de Dados

Vamos gerar um conjunto de dados de 3 classes usando a função `make_blobs` do scikit-learn. Usaremos 1000 amostras e definiremos os centros dos blobs em `[-5, 0], [0, 1.5], [5, -1]`. Em seguida, transformaremos o conjunto de dados usando uma matriz de transformação para tornar o conjunto de dados mais difícil de classificar.

```python
centers = [[-5, 0], [0, 1.5], [5, -1]]
X, y = make_blobs(n_samples=1000, centers=centers, random_state=40)
transformation = [[0.4, 0.2], [-0.4, 1.2]]
X = np.dot(X, transformation)
```
