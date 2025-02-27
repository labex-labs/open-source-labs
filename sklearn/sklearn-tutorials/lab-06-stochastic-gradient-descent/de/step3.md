# Daten vorverarbeiten

Bevor der SGD angewendet wird, ist es oft vorteilhaft, die Daten vorzubehandeln. In diesem Fall werden wir die Merkmale mit dem StandardScaler aus scikit-learn standardisieren.

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
```