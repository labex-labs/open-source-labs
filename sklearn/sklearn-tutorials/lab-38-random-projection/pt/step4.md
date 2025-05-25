# Projeção aleatória esparsa

Em seguida, vamos experimentar outro tipo de projeção aleatória chamada projeção aleatória esparsa.

```python
transformer = random_projection.SparseRandomProjection()
X_new = transformer.fit_transform(X)
```

Aqui, criamos uma instância da classe `SparseRandomProjection` e a aplicamos aos nossos dados `X` usando o método `fit_transform`. O resultado é armazenado na variável `X_new`.
