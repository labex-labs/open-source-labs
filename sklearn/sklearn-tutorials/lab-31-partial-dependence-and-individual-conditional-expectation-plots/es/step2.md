# Cargar y preparar los datos

```python
data = load_boston()
X = data.data
y = data.target
feature_names = data.feature_names

# Crear un DataFrame para una manipulación de datos más fácil
df = pd.DataFrame(X, columns=feature_names)
```
