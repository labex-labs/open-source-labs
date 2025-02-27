# Eindeutige Merkmalsimputation mit SimpleImputer

Die Klasse `SimpleImputer` bietet grundlegende Strategien zur Imputation fehlender Werte auf eindimensionale Weise. Wir können verschiedene Strategien wählen, wie zum Beispiel das Ersetzen fehlender Werte mit einem konstanten Wert oder das Verwenden des Mittelwerts, des Medianwerts oder des häufigsten Werts jeder Spalte, um die fehlenden Werte zu imputieren.

Lassen Sie uns mit der Mittelwertstrategie beginnen. Wir werden eine Instanz von `SimpleImputer` erstellen und sie auf unseren Daten anpassen, um die Imputationsstrategie zu lernen. Anschließend können wir die `transform`-Methode verwenden, um die fehlenden Werte auf der Grundlage der gelernten Strategie zu imputieren.

```python
imp = SimpleImputer(strategy='mean')
X = [[1, 2], [np.nan, 3], [7, 6]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [7, 6]]
imputed_X_test = imp.transform(X_test)
```
