# Darstellung der Ergebnisse

Jetzt ordnen wir die Daten basierend auf den Zeilen- und Spaltenbezeichnungen, die vom `SpectralBiclustering`-Modell zugewiesen wurden, in aufsteigender Reihenfolge neu an und plotten sie erneut. Die `row_labels_` reichen von 0 bis 3, während die `column_labels_` von 0 bis 2 reichen, was insgesamt 4 Cluster pro Zeile und 3 Cluster pro Spalte repräsentiert.

```python
# Zuerst die Zeilen und dann die Spalten neu ordnen.
reordered_rows = data[np.argsort(model.row_labels_)]
reordered_data = reordered_rows[:, np.argsort(model.column_labels_)]

plt.matshow(reordered_data, cmap=plt.cm.Blues)
plt.title("Nach der Biclustering; neu angeordnet, um die Bicluster zu zeigen")
_ = plt.show()
```

Als letztes möchten wir die Beziehungen zwischen den Zeilen- und Spaltenbezeichnungen, die vom Modell zugewiesen wurden, demonstrieren. Daher erstellen wir ein Gitter mit `numpy.outer`, das die sortierten `row_labels_` und `column_labels_` nimmt und 1 zu jedem hinzuaddiert, um sicherzustellen, dass die Bezeichnungen bei 1 anfangen statt bei 0 für eine bessere Visualisierung.

```python
plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap=plt.cm.Blues,
)
plt.title("Schachbrett-Struktur der neu angeordneten Daten")
plt.show()
```
