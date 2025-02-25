# Eigenschaften festlegen

Die pyplot-Schnittstelle ermöglicht es uns, Objekteigenschaften für die Visualisierung von Daten festzulegen und abzurufen. Wir können die `setp`-Methode verwenden, um die Eigenschaften eines Objekts festzulegen. Beispielsweise um den Linienstil einer Linie auf gestrichelt zu setzen, verwenden wir folgenden Code:

```python
line, = plt.plot([1, 2, 3])
plt.setp(line, linestyle='--')
```

Wenn wir wissen möchten, welche gültigen Argumenttypen es gibt, können wir den Namen der Eigenschaft, die wir festlegen möchten, ohne einen Wert angeben:

```python
plt.setp(line, 'linestyle')
```

Dies liefert die folgende Ausgabe:

```
linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq),...}
```

Wenn wir alle Eigenschaften, die festgelegt werden können, und deren mögliche Werte anzeigen möchten, können wir folgenden Code verwenden:

```python
plt.setp(line)
```

Dies liefert eine lange Liste von Eigenschaften und deren möglichen Werten.
