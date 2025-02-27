# Решательные поверхности ядра SVM с RBF и линейного SVM

```python
# визуализируем решательную поверхность, проектированную на первые
# два главных компонента датасета
pca = PCA(n_components=8).fit(data_train)

X = pca.transform(data_train)

# Генерируем сетку вдоль первых двух главных компонентов
multiples = np.arange(-2, 2, 0.1)
# шаги вдоль первой компоненты
first = multiples[:, np.newaxis] * pca.components_[0, :]
# шаги вдоль второй компоненты
second = multiples[:, np.newaxis] * pca.components_[1, :]
# объединяем
grid = first[np.newaxis, :, :] + second[:, np.newaxis, :]
flat_grid = grid.reshape(-1, data.shape[1])

# заголовок для графиков
titles = [
    "SVC с rbf ядром",
    "SVC (линейное ядро)\n с Fourier rbf картой признаков\nn_components=100",
    "SVC (линейное ядро)\n с Nystroem rbf картой признаков\nn_components=100",
]

plt.figure(figsize=(18, 7.5))
plt.rcParams.update({"font.size": 14})
# предсказываем и рисуем
for i, clf in enumerate((kernel_svm, nystroem_approx_svm, fourier_approx_svm)):
    # Рисуем границу решения. Для этого мы присвоим цвет каждой
    # точке в сетке [x_min, x_max]x[y_min, y_max].
    plt.subplot(1, 3, i + 1)
    Z = clf.predict(flat_grid)

    # Помещаем результат в цветовую диаграмму
    Z = Z.reshape(grid.shape[:-1])
    levels = np.arange(10)
    lv_eps = 0.01  # Настройте отображение между вычисленными уровнями контура и цветом.
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

    # Также рисуем обучающие точки
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
