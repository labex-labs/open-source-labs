# Preparar los datos

Ahora prepararemos los datos para la estimación de densidad de núcleo. Extraeremos la información de latitud y longitud del conjunto de datos y la convertiremos a radianes.

```python
Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # Convertir lat/long a radianes
```
