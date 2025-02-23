# Establecer semilla aleatoria y contenedores

Establece una semilla aleatoria para la reproducibilidad y fija los bordes de los contenedores.

```python
# Fijando el estado aleatorio para la reproducibilidad
np.random.seed(19680801)

# Fijando los bordes de los contenedores
HIST_BINS = np.linspace(-4, 4, 100)
```
