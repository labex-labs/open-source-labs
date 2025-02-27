# Eigenfaces visualisieren

```python
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

Wir plotten auch die Eigenfaces, um die aus den Eingabedaten extrahierten Merkmale zu visualisieren.