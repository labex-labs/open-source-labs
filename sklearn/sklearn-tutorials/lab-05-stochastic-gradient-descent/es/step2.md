# Cargar y preprocesar los datos

A continuación, cargaremos el conjunto de datos iris y lo preprocesaremos escalando las características utilizando StandardScaler.

```python
# Cargar el conjunto de datos iris
iris = load_iris()
X, y = iris.data, iris.target

# Escalar las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```
