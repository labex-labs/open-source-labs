# Visualizar eigenfaces

```python
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

También graficamos las eigenfaces para visualizar las características extraídas de los datos de entrada.
