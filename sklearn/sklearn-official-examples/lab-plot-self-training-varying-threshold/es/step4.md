# Definir valores de umbral

```python
x_values = np.arange(0.4, 1.05, 0.05)
x_values = np.append(x_values, 0.99999)
```

Definimos una matriz de valores de umbral que van desde 0.4 hasta 1, con pasos de 0.05. Luego agregamos un valor de umbral muy alto de 0.99999 para asegurarnos de incluir un valor de umbral que no resultará en ninguna muestra autoetiquetada.
