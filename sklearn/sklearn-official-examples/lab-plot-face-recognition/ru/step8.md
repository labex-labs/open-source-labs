# Визуализация собственных лиц (eigenfaces)

```python
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

Мы также строим графики собственных лиц (eigenfaces), чтобы визуализировать признаки, извлеченные из входных данных.
