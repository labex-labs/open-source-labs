# Transformação inversa

Os transformadores de projeção aleatória têm a opção de calcular a inversa da matriz de projeção. Vamos explorar este recurso aplicando a transformação inversa aos nossos dados projetados.

```python
transformer = random_projection.SparseRandomProjection(compute_inverse_components=True)
X_new = transformer.fit_transform(X)

# Calcular a transformação inversa
X_new_inversed = transformer.inverse_transform(X_new)
```

Nesta etapa, criamos uma instância da classe `SparseRandomProjection` com o parâmetro `compute_inverse_components` definido como `True`. Em seguida, ajustamos o transformador aos nossos dados `X` e aplicamos a transformação. Finalmente, calculamos a transformação inversa chamando o método `inverse_transform` nos dados projetados `X_new`.
