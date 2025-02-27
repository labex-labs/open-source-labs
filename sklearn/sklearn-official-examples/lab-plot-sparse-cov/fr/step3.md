# Tracer les résultats

La troisième étape consiste à tracer les résultats. Nous traçons les covariances et les précisions. Nous traçons également la métrique de sélection de modèle.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.subplots_adjust(left=0.02, right=0.98)

# tracer les covariances
covs = [
    ("Empirique", emp_cov),
    ("Ledoit-Wolf", lw_cov_),
    ("GraphicalLassoCV", cov_),
    ("Vraie", cov),
]
vmax = cov_.max()
for i, (nom, cette_cov) in enumerate(covs):
    plt.subplot(2, 4, i + 1)
    plt.imshow(
        cette_cov, interpolation="proche", vmin=-vmax, vmax=vmax, cmap=plt.cm.RdBu_r
    )
    plt.xticks(())
    plt.yticks(())
    plt.title("%s covariance" % nom)


# tracer les précisions
precs = [
    ("Empirique", linalg.inv(emp_cov)),
    ("Ledoit-Wolf", lw_prec_),
    ("GraphicalLasso", prec_),
    ("Vraie", prec),
]
vmax = 0.9 * prec_.max()
for i, (nom, cette_prec) in enumerate(precs):
    ax = plt.subplot(2, 4, i + 5)
    plt.imshow(
        np.ma.masked_equal(cette_prec, 0),
        interpolation="proche",
        vmin=-vmax,
        vmax=vmax,
        cmap=plt.cm.RdBu_r,
    )
    plt.xticks(())
    plt.yticks(())
    plt.title("%s précision" % nom)
    if hasattr(ax, "set_facecolor"):
        ax.set_facecolor(".7")
    else:
        ax.set_axis_bgcolor(".7")

# tracer la métrique de sélection de modèle
plt.figure(figsize=(4, 3))
plt.axes([0.2, 0.15, 0.75, 0.7])
plt.plot(model.cv_results_["alphas"], model.cv_results_["mean_test_score"], "o-")
plt.axvline(model.alpha_, color=".5")
plt.title("Sélection de modèle")
plt.ylabel("Score de validation croisée")
plt.xlabel("alpha")

plt.show()
```
