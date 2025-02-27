# Generar datos densos

A continuación, generamos algunos datos densos que usaremos para la regresión Lasso. Utilizamos la función `make_regression` de Scikit-learn para generar 200 muestras con 5000 características.

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```
