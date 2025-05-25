# Visualizar Eigenfaces

```python
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

Também plotamos os eigenfaces para visualizar as características extraídas dos dados de entrada.
