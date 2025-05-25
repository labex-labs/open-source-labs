# Verificação

Para verificar a correção da transformação inversa, podemos comparar os dados originais `X` com o resultado da transformação inversa.

```python
X_new_again = transformer.transform(X_new_inversed)
np.allclose(X_new, X_new_again)
```

Aqui, aplicamos a transformação aos dados transformados inversamente `X_new_inversed` e verificamos se é igual aos dados projetados originais `X_new` usando a função `np.allclose`.
