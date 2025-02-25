# Zusammenfassung

In diesem Lab haben wir gelernt, wie man die Bibliothek `multiprocessing` und Matplotlib verwendet, um Daten zu visualisieren, die aus einem separaten Prozess generiert wurden. Wir haben zwei Klassen - `ProcessPlotter` und `NBPlot` - erstellt, um die Visualisierung und die Datengenerierung zu verarbeiten. Die Klasse `NBPlot` generiert zufällige Daten und sendet sie an die Klasse `ProcessPlotter` über eine Pipe, die dann die Daten in Echtzeit visualisiert.
