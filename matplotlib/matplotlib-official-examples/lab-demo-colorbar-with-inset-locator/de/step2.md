# Erstellen eines Diagramms und eines Bildes

Als nächstes werden wir ein Diagramm und ein Bild erstellen, um zu zeigen, wie man eine Farbskala mit Hilfe von Einfügebereichen hinzufügt.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[6, 3])

im1 = ax1.imshow([[1, 2], [2, 3]])
im2 = ax2.imshow([[1, 2], [2, 3]])
```
