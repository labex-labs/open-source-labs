# Representar los resultados

El tercer paso es representar los resultados. Representamos las covarianzas y las precisiones. También representamos la métrica de selección de modelo.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.subplots_adjust(left=0.02, right=0.98)

# representar las covarianzas
covs = [
    ("Empírica", emp_cov),
    ("Ledoit-Wolf", lw_cov_),
    ("GraphicalLassoCV", cov_),
    ("Verdadera", cov),
]
vmax = cov_.max()
for i, (nombre, esta_cov) in enumerate(covs):
    plt.subplot(2, 4, i + 1)
    plt.imshow(
        esta_cov, interpolation="nearest", vmin=-vmax, vmax=vmax, cmap=plt.cm.RdBu_r
    )
    plt.xticks(())
    plt.yticks(())
    plt.title("%s covarianza" % nombre)


# representar las precisiones
precs = [
    ("Empírica", linalg.inv(emp_cov)),
    ("Ledoit-Wolf", lw_prec_),
    ("GraphicalLasso", prec_),
    ("Verdadera", prec),
]
vmax = 0.9 * prec_.max()
for i, (nombre, esta_prec) in enumerate(precs):
    ax = plt.subplot(2, 4, i + 5)
    plt.imshow(
        np.ma.masked_equal(esta_prec, 0),
        interpolation="nearest",
        vmin=-vmax,
        vmax=vmax,
        cmap=plt.cm.RdBu_r,
    )
    plt.xticks(())
    plt.yticks(())
    plt.title("%s precisión" % nombre)
    if hasattr(ax, "set_facecolor"):
        ax.set_facecolor(".7")
    else:
        ax.set_axis_bgcolor(".7")

# representar la métrica de selección de modelo
plt.figure(figsize=(4, 3))
plt.axes([0.2, 0.15, 0.75, 0.7])
plt.plot(model.cv_results_["alphas"], model.cv_results_["mean_test_score"], "o-")
plt.axvline(model.alpha_, color=".5")
plt.title("Selección de modelo")
plt.ylabel("Puntuación de validación cruzada")
plt.xlabel("alpha")

plt.show()
```
