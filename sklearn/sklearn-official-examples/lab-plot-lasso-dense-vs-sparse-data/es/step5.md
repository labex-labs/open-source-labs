# Comparar los coeficientes del Lasso denso y el Lasso disperso

Comparamos los coeficientes del modelo Lasso denso y el modelo Lasso disperso para asegurarnos de que estén produciendo los mismos resultados. Calculamos la norma Euclidiana de la diferencia entre los coeficientes.

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distancia entre los coeficientes : {coeff_diff:.2e}")
```
