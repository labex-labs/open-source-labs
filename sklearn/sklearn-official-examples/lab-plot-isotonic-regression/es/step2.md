# Generar datos

A continuación, generaremos algunos datos para utilizar en nuestra regresión. Crearemos una tendencia no lineal monótona con ruido uniforme homoscedástico.

```python
n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50.0 * np.log1p(np.arange(n))
```
