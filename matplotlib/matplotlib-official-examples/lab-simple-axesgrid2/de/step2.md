# Erstellen einer Figur und eines ImageGrid

Als nächstes erstellen wir eine Figur und ein ImageGrid mit dem Parameter `nrows_ncols`, um die Anzahl der Zeilen und Spalten des Gitters zu definieren.

```python
fig = plt.figure(figsize=(5.5, 3.5))
grid = ImageGrid(fig, 111,  # ähnlich wie subplot(111)
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,
                 label_mode="L")
```
