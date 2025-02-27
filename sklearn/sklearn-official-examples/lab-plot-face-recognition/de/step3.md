# Datenaufbereitung

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Wir teilen den Datensatz in einen Trainingssatz und einen Testsatz auf und bereiten die Daten durch Skalierung der Eingabedaten mit der Funktion `StandardScaler()` auf.