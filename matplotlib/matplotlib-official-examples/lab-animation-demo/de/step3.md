# Die Animation erstellen

Wir werden eine for-Schleife verwenden, um durch jede Frame der Animation zu iterieren. In jeder Iteration werden wir die Achse löschen, das aktuelle Frame plotten, den Titel setzen und für eine kurze Zeit pausieren, um die Animation anzeigen zu lassen.

```python
fig, ax = plt.subplots()

for i, img in enumerate(data):
    ax.clear()
    ax.imshow(img)
    ax.set_title(f"frame {i}")
    plt.pause(0.1)
```
