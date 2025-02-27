# Eigenfaces (Eigengesichter) visualisieren

```python
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

Wir stellen auch die Eigenfaces (Eigengesichter) dar, um die aus den Eingabedaten extrahierten Merkmale zu visualisieren.
