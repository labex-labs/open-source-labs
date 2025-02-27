# Ergebnisse plotten

Wir plotten die ursprünglichen Ziffern und die neu resamplten Ziffern nebeneinander in einem 4x11-Gitter.

```python
import matplotlib.pyplot as plt

# wandeln Sie die Daten in ein 4x11-Gitter um
new_data = new_data.reshape((4, 11, -1))
real_data = digits.data[:44].reshape((4, 11, -1))

# plotten Sie die echten Ziffern und die neu resamplten Ziffern
fig, ax = plt.subplots(9, 11, subplot_kw=dict(xticks=[], yticks=[]))
for j in range(11):
    ax[4, j].set_visible(False)
    for i in range(4):
        im = ax[i, j].imshow(
            real_data[i, j].reshape((8, 8)), cmap=plt.cm.binary, interpolation="nearest"
        )
        im.set_clim(0, 16)
        im = ax[i + 5, j].imshow(
            new_data[i, j].reshape((8, 8)), cmap=plt.cm.binary, interpolation="nearest"
        )
        im.set_clim(0, 16)

ax[0, 5].set_title("Auswahl aus den Eingabedaten")
ax[5, 5].set_title('"Neue" Ziffern, die aus dem Kernel-Dichtemodell gezogen wurden')

plt.show()
```
