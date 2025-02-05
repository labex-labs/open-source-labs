# Visualize Eigenfaces

```python
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

We also plot the eigenfaces to visualize the features extracted from the input data.
