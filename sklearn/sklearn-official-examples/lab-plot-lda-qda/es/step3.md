# Funciones de trazado

Definiremos dos funciones para trazar los datos y las elipses.

```python
def plot_data(lda, X, y, y_pred, fig_index):
    splot = plt.subplot(2, 2, fig_index)
    if fig_index == 1:
        plt.title("Análisis Discriminante Lineal")
        plt.ylabel("Datos con\n covarianza fija")
    elif fig_index == 2:
        plt.title("Análisis Discriminante Cuadrático")
    elif fig_index == 3:
        plt.ylabel("Datos con\n covarianzas variables")

    tp = y == y_pred  # Verdadero Positivo
    tp0, tp1 = tp[y == 0], tp[y == 1]
    X0, X1 = X[y == 0], X[y == 1]
    X0_tp, X0_fp = X0[tp0], X0[~tp0]
    X1_tp, X1_fp = X1[tp1], X1[~tp1]

    # clase 0: puntos
    plt.scatter(X0_tp[:, 0], X0_tp[:, 1], marker=".", color="red")
    plt.scatter(X0_fp[:, 0], X0_fp[:, 1], marker="x", s=20, color="#990000")  # rojo oscuro

    # clase 1: puntos
    plt.scatter(X1_tp[:, 0], X1_tp[:, 1], marker=".", color="blue")
    plt.scatter(X1_fp[:, 0], X1_fp[:, 1], marker="x", s=20, color="#000099")  # azul oscuro

    # clase 0 y 1 : áreas
    nx, ny = 200, 100
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny))
    Z = lda.predict_proba(np.c_[xx.ravel(), yy.ravel()])
    Z = Z[:, 1].reshape(xx.shape)
    plt.pcolormesh(xx, yy, Z, cmap="red_blue_classes", norm=colors.Normalize(0.0, 1.0), zorder=0)
    plt.contour(xx, yy, Z, [0.5], linewidths=2.0, colors="white")

    # medias
    plt.plot(lda.means_[0][0], lda.means_[0][1], "*", color="yellow", markersize=15, markeredgecolor="grey")
    plt.plot(lda.means_[1][0], lda.means_[1][1], "*", color="yellow", markersize=15, markeredgecolor="grey")

    return splot


def plot_ellipse(splot, mean, cov, color):
    v, w = linalg.eigh(cov)
    u = w[0] / linalg.norm(w[0])
    angle = np.arctan(u[1] / u[0])
    angle = 180 * angle / np.pi  # convertir a grados
    # Gaussiana rellena a 2 desviaciones estándar
    ell = mpl.patches.Ellipse(mean, 2 * v[0] ** 0.5, 2 * v[1] ** 0.5, angle=180 + angle, facecolor=color, edgecolor="black", linewidth=2)
    ell.set_clip_box(splot.bbox)
    ell.set_alpha(0.2)
    splot.add_artist(ell)
    splot.set_xticks(())
    splot.set_yticks(())
```
