# Generar datos

A continuación, generará algunos datos de muestra. En este laboratorio, generaremos una onda senoidal bidimensional.

```python
t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
```
