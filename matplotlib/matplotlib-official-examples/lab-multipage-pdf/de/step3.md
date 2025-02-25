# Erstellen der ersten Seite

In diesem Schritt wirst du die erste Seite der PDF-Datei erstellen. Die Seite wird einen Plot eines einfachen Graphen enthalten.

```python
plt.figure(figsize=(3, 3))
plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
plt.title('Page One')
pdf.savefig()
plt.close()
```
