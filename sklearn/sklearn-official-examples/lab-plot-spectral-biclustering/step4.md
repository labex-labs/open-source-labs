# Plotting results

Now, we rearrange the data based on the row and column labels assigned by the `SpectralBiclustering` model in ascending order and plot again. The `row_labels_` range from 0 to 3, while the `column_labels_` range from 0 to 2, representing a total of 4 clusters per row and 3 clusters per column.

```python
# Reordering first the rows and then the columns.
reordered_rows = data[np.argsort(model.row_labels_)]
reordered_data = reordered_rows[:, np.argsort(model.column_labels_)]

plt.matshow(reordered_data, cmap=plt.cm.Blues)
plt.title("After biclustering; rearranged to show biclusters")
_ = plt.show()
```

As a last step, we want to demonstrate the relationships between the row and column labels assigned by the model. Therefore, we create a grid with `numpy.outer`, which takes the sorted `row_labels_` and `column_labels_` and adds 1 to each to ensure that the labels start from 1 instead of 0 for better visualization.

```python
plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap=plt.cm.Blues,
)
plt.title("Checkerboard structure of rearranged data")
plt.show()
```
