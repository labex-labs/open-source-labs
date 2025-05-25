# Codificação Esparsa

Vamos realizar codificação esparsa no sinal usando diferentes métodos e visualizar os resultados.

```python
# Lista os diferentes métodos de codificação esparsa no seguinte formato:
# (título, algoritmo_transformação, alpha_transformação,
#  n_coefs_não_zero_transformação, cor)
estimators = [
    ("OMP", "omp", None, 15, "navy"),
    ("Lasso", "lasso_lars", 2, None, "turquoise"),
]
lw = 2

plt.figure(figsize=(13, 6))
for subplot, (D, title) in enumerate(
    zip((D_fixed, D_multi), ("largura fixa", "larguras múltiplas"))
):
    plt.subplot(1, 2, subplot + 1)
    plt.title("Codificação esparsa contra dicionário %s" % title)
    plt.plot(y, lw=lw, linestyle="--", label="Sinal original")
    # Faz uma aproximação wavelet
    for title, algo, alpha, n_nonzero, color in estimators:
        coder = SparseCoder(
            dictionary=D,
            transform_n_nonzero_coefs=n_nonzero,
            transform_alpha=alpha,
            transform_algorithm=algo,
        )
        x = coder.transform(y.reshape(1, -1))
        density = len(np.flatnonzero(x))
        x = np.ravel(np.dot(x, D))
        squared_error = np.sum((y - x) ** 2)
        plt.plot(
            x,
            color=color,
            lw=lw,
            label="%s: %s coefs não nulos,\n%.2f erro" % (title, density, squared_error),
        )

    # Desvios de limiarização suave
    coder = SparseCoder(
        dictionary=D, transform_algorithm="threshold", transform_alpha=20
    )
    x = coder.transform(y.reshape(1, -1))
    _, idx = np.where(x != 0)
    x[0, idx], _, _, _ = np.linalg.lstsq(D[idx, :].T, y, rcond=None)
    x = np.ravel(np.dot(x, D))
    squared_error = np.sum((y - x) ** 2)
    plt.plot(
        x,
        color="darkorange",
        lw=lw,
        label="Limiarização com desvio:\n%d coefs não nulos, %.2f erro"
        % (len(idx), squared_error),
    )
    plt.axis("tight")
    plt.legend(shadow=False, loc="best")
plt.subplots_adjust(0.04, 0.07, 0.97, 0.90, 0.09, 0.2)
plt.show()
```
