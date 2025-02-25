# Convertir coordenadas polares a coordenadas cartesianas

Convertiremos las coordenadas polares a coordenadas cartesianas:

```python
# Convertir las coordenadas polares (radios, ángulos) a coordenadas cartesianas (x, y).
# (0, 0) se agrega manualmente en esta etapa, para que no haya puntos duplicados
# en el plano (x, y).
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())
```
