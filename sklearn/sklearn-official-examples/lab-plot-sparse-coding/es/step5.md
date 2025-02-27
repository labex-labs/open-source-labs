# Codificación esparsa

Realizaremos la codificación esparsa en la señal utilizando diferentes métodos y visualizaremos los resultados.

```python
# Liste los diferentes métodos de codificación esparsa en el siguiente formato:
# (título, algoritmo de transformación, alfa de transformación,
#  número de coeficientes no nulos de transformación, color)
estimadores = [
    ("OMP", "omp", None, 15, "azul marino"),
    ("Lasso", "lasso_lars", 2, None, "turquesa"),
]
lw = 2

plt.figure(figsize=(13, 6))
for subplot, (D, título) in enumerate(
    zip((D_fixed, D_multi), ("ancho fijo", "varios anchos"))
):
    plt.subplot(1, 2, subplot + 1)
    plt.title("Codificación esparsa contra el diccionario %s" % título)
    plt.plot(y, lw=lw, linestyle="--", label="Señal original")
    # Haga una aproximación de ondas
    for título, algo, alfa, n_no_nulos, color in estimadores:
        codificador = SparseCoder(
            dictionary=D,
            transform_n_nonzero_coefs=n_no_nulos,
            transform_alpha=alfa,
            transform_algorithm=algo,
        )
        x = codificador.transform(y.reshape(1, -1))
        densidad = len(np.flatnonzero(x))
        x = np.ravel(np.dot(x, D))
        error_cuadrado = np.sum((y - x) ** 2)
        plt.plot(
            x,
            color=color,
            lw=lw,
            label="%s: %s coeficientes no nulos,\n%.2f error" % (título, densidad, error_cuadrado),
        )

    # Desviación de umbral suave
    codificador = SparseCoder(
        dictionary=D, transform_algorithm="umbral", transform_alpha=20
    )
    x = codificador.transform(y.reshape(1, -1))
    _, idx = np.where(x!= 0)
    x[0, idx], _, _, _ = np.linalg.lstsq(D[idx, :].T, y, rcond=None)
    x = np.ravel(np.dot(x, D))
    error_cuadrado = np.sum((y - x) ** 2)
    plt.plot(
        x,
        color="naranja oscura",
        lw=lw,
        label="Umbralización con desviación:\n%d coeficientes no nulos, %.2f error"
        % (len(idx), error_cuadrado),
    )
    plt.axis("tight")
    plt.legend(shadow=False, loc="mejor")
plt.subplots_adjust(0.04, 0.07, 0.97, 0.90, 0.09, 0.2)
plt.show()
```
