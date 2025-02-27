# Datenvorverarbeitung

Bevor wir SGD anwenden, ist es oft vorteilhaft, die Daten vorzuverarbeiten. In diesem Fall werden wir die Merkmale (Features) mit Hilfe von scikit-learns `StandardScaler` standardisieren.

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
```
