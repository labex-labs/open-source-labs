# Die vervollständigten Gesichter plotten

Der letzte Schritt besteht darin, die vervollständigten Gesichter für jeden Algorithmus zu plotten und sie mit den ursprünglichen Gesichtern zu vergleichen. Die ursprünglichen Gesichter werden in der ersten Spalte gezeigt, und die vervollständigten Gesichter werden in den nachfolgenden Spalten für jeden Algorithmus gezeigt. Die Leistung der Algorithmen kann durch Vergleich der vervollständigten Gesichter mit den ursprünglichen Gesichtern bewertet werden.

```python
# Plot the completed faces
image_shape = (64, 64)

n_cols = 1 + len(ESTIMATORS)
plt.figure(figsize=(2.0 * n_cols, 2.26 * n_faces))
plt.suptitle("Face completion with multi-output estimators", size=16)

for i in range(n_faces):
    true_face = np.hstack((X_test[i], y_test[i]))

    if i:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1)
    else:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1, title="true faces")

    sub.axis("off")
    sub.imshow(
        true_face.reshape(image_shape), cmap=plt.cm.gray, interpolation="nearest"
    )

    for j, est in enumerate(sorted(ESTIMATORS)):
        completed_face = np.hstack((X_test[i], y_test_predict[est][i]))

        if i:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j)

        else:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j, title=est)

        sub.axis("off")
        sub.imshow(
            completed_face.reshape(image_shape),
            cmap=plt.cm.gray,
            interpolation="nearest",
        )

plt.show()
```
