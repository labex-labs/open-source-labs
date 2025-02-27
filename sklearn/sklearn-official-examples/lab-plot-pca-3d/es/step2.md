# Crear datos

Generaremos un conjunto de datos aleatorios para este laboratorio. El conjunto de datos tendrá tres variables: `x`, `y` y `z`. Definiremos `x` e `y` como variables aleatorias con distribución normal, con media 0 y desviación estándar de 0,5. `z` también tiene una distribución normal con media 0 y desviación estándar de 0,1.

```python
e = np.exp(1)
np.random.seed(4)

y = np.random.normal(scale=0.5, size=(30000))
x = np.random.normal(scale=0.5, size=(30000))
z = np.random.normal(scale=0.1, size=len(x))
```
