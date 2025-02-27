# Creando un objeto de búsqueda aleatoria por mitades

Crea un objeto `HalvingRandomSearchCV` para buscar en el espacio de parámetros. El objeto toma los siguientes argumentos:

- `estimator`: el estimador a optimizar
- `param_distributions`: el espacio de parámetros para buscar
- `factor`: el factor por el cual se reduce el número de candidatos en cada iteración
- `random_state`: el estado aleatorio utilizado para la búsqueda

El código para crear el objeto es el siguiente:

```python
clf = RandomForestClassifier(n_estimators=20, random_state=rng)
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
```
