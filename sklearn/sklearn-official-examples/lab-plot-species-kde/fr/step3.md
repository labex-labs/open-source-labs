# Préparer les données

Nous allons maintenant préparer les données pour l'estimation de la densité de noyau. Nous allons extraire les informations de latitude et de longitude à partir de l'ensemble de données et les convertir en radians.

```python
Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # Convert lat/long to radians
```
