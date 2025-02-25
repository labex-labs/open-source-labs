# Creando datos

A continuación, crearemos algunos datos para nuestros gráficos. En este ejemplo, crearemos tres ondas sinusoidales con diferentes frecuencias.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(3*np.pi*t)
s3 = np.sin(4*np.pi*t)
```
