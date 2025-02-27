# Daten vorbereiten

Wir bereiten nun die Daten für die Kernel-Dichteschätzung vor. Wir extrahieren die Längen- und Breitengradinformationen aus dem Datensatz und konvertieren sie in Radiant.

```python
Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # Convert lat/long to radians
```
