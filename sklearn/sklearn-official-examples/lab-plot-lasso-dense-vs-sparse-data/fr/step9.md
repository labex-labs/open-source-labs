# Comparer les coefficients du Lasso dense et du Lasso creux

Nous comparons les coefficients du modèle Lasso dense et du modèle Lasso creux pour nous assurer qu'ils produisent les mêmes résultats. Nous calculons la norme euclidienne de la différence entre les coefficients.

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distance entre les coefficients : {coeff_diff:.2e}")
```
