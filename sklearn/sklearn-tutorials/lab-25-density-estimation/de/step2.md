# Generieren von Beispiel-Daten

Als nächstes werden wir einige Beispiel-Daten generieren, auf denen wir die Dichteschätzung durchführen werden. Zu Zwecken dieses Labs generieren wir einen eindimensionalen Datensatz mit 100 Punkten. Wir werden eine Normalverteilung verwenden, um die Daten zu generieren.

```python
np.random.seed(0)
X = np.random.normal(0, 1, 100).reshape(-1, 1)
```
