# Crear datos

A continuación, crearemos los datos que se utilizarán en la gráfica. Crearemos tres diferentes ondas senoidales con diferentes frecuencias utilizando la biblioteca `numpy`.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)
```
