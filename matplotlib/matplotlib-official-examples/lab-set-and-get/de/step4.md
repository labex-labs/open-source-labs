# Eigenschaften abrufen

Wir können die `getp`-Methode verwenden, um die Eigenschaften eines Objekts abzurufen. Wir können sie verwenden, um den Wert eines einzelnen Attributs abzufragen:

```python
plt.getp(line, 'linewidth')
```

Dies wird den Wert der Zeilenstärke-Eigenschaft des Linieobjekts zurückgeben.

Wir können `getp` auch verwenden, um alle Attribut-/Wert-Paare eines Objekts abzurufen:

```python
plt.getp(line)
```

Dies wird eine lange Liste aller Eigenschaften und ihrer Werte zurückgeben.
