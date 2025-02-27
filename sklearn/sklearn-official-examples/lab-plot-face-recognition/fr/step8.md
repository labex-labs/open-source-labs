# Visualiser les eigenfaces

```python
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

Nous traçons également les eigenfaces pour visualiser les caractéristiques extraites des données d'entrée.
