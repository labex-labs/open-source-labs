# Laden und Vorbereiten der Daten

```python
data = load_boston()
X = data.data
y = data.target
feature_names = data.feature_names

# Erstellen eines DataFrames für eine einfachere Datenmanipulation
df = pd.DataFrame(X, columns=feature_names)
```
