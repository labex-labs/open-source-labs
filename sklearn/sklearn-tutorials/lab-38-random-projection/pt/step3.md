# Projeção aleatória gaussiana

Agora, vamos aplicar a projeção aleatória gaussiana para reduzir a dimensionalidade dos nossos dados.

```python
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
```

Nesta etapa, criamos uma instância da classe `GaussianRandomProjection` e a ajustamos aos nossos dados `X`. Em seguida, aplicamos a transformação chamando o método `fit_transform`. O resultado é armazenado na variável `X_new`.
