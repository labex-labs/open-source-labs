# Imputación de características univariadas utilizando SimpleImputer

La clase `SimpleImputer` proporciona estrategias básicas para imputar valores faltantes de manera univariada. Podemos elegir entre diferentes estrategias, como reemplazar los valores faltantes con un valor constante o utilizar la media, la mediana o el valor más frecuente de cada columna para imputar los valores faltantes.

Comencemos considerando la estrategia de la media. Crearemos una instancia de `SimpleImputer` y la ajustaremos a nuestros datos para aprender la estrategia de imputación. Luego, podemos utilizar el método `transform` para imputar los valores faltantes en base a la estrategia aprendida.

```python
imp = SimpleImputer(strategy='mean')
X = [[1, 2], [np.nan, 3], [7, 6]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [7, 6]]
imputed_X_test = imp.transform(X_test)
```
