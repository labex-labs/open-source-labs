# Parámetros Anidados

Puede acceder a los parámetros de los estimadores en una tubería utilizando la sintaxis `<estimador>__<parámetro>`. Esto es útil para realizar búsquedas en cuadrícula sobre los parámetros de todos los estimadores en la tubería. Aquí hay un ejemplo:

```python
pipe.set_params(clf__C=10)
```
