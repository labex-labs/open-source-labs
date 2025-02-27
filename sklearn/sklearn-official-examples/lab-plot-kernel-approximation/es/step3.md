# Superficies de decisión del SVM con kernel RBF y del SVM lineal

```python
# visualizar la superficie de decisión, proyectada hacia los primeros
# dos componentes principales del conjunto de datos
pca = PCA(n_components=8).fit(data_train)

X = pca.transform(data_train)

# Generar una cuadrícula a lo largo de los primeros dos componentes principales
multiples = np.arange(-2, 2, 0.1)
# pasos a lo largo del primer componente
first = multiples[:, np.newaxis] * pca.components_[0, :]
# pasos a lo largo del segundo componente
second = multiples[:, np.newaxis] * pca.components_[1, :]
# combinar
grid = first[np.newaxis, :, :] + second[:, np.newaxis, :]
flat_grid = grid.reshape(-1, data.shape[1])

# título para las gráficas
titles = [
    "SVC con kernel rbf",
    "SVC (kernel lineal)\n con mapa de características rbf de Fourier\nn_componentes=100",
    "SVC (kernel lineal)\n con mapa de características rbf de Nystroem\nn_componentes=100",
]

plt.figure(figsize=(18, 7.5))
plt.rcParams.update({"font.size": 14})
# predecir y graficar
for i, clf in enumerate((kernel_svm, nystroem_approx_svm, fourier_approx_svm)):
    # Graficar el límite de decisión. Para eso, asignaremos un color a cada
    # punto en la malla [x_min, x_max]x[y_min, y_max].
    plt.subplot(1, 3, i + 1)
    Z = clf.predict(flat_grid)

    # Poner el resultado en una gráfica de color
    Z = Z.reshape(grid.shape[:-1])
    levels = np.arange(10)
    lv_eps = 0.01  # Ajustar una asignación de los niveles de contorno calculados al color.
    plt.contourf(
        multiples,
        multiples,
        Z,
        levels=levels - lv_eps,
        cmap=plt.cm.tab10,
        vmin=0,
        vmax=10,
        alpha=0.7,
    )
    plt.axis("off")

    # Graficar también los puntos de entrenamiento
    plt.scatter(
        X[:, 0],
        X[:, 1],
        c=targets_train,
        cmap=plt.cm.tab10,
        edgecolors=(0, 0, 0),
        vmin=0,
        vmax=10,
    )

    plt.title(titles[i])
plt.tight_layout()
plt.show()
```
