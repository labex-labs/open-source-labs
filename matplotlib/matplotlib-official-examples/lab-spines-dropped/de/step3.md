# Erstellen einer Figur und Achsen

Wir erstellen eine Figur und ein Achsenobjekt mit `plt.subplots()`. Die `imshow()`-Funktion wird verwendet, um die zufälligen Daten als Bild anzuzeigen.

```python
fig, ax = plt.subplots()

image = np.random.uniform(size=(10, 10))
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('dropped spines')
```
