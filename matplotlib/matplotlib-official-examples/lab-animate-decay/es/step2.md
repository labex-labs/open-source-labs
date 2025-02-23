# Crear la función generadora de datos

A continuación, necesitamos crear una función para generar los datos de la animación. La función producirá una onda senoidal que decae con el tiempo. Utilizaremos la función `itertools.count()` para generar una secuencia infinita de números. Utilizaremos estos números para calcular los valores de la onda senoidal.

```python
def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
```
