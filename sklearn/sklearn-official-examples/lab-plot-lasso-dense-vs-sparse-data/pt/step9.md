# Comparar Coeficientes de Lasso Denso e Lasso Esparso

Comparamos os coeficientes do modelo Lasso denso e do modelo Lasso esparso para garantir que estão produzindo os mesmos resultados. Calculamos a norma euclidiana da diferença entre os coeficientes.

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distância entre coeficientes : {coeff_diff:.2e}")
```
