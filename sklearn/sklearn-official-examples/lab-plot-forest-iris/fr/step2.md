# Définition des paramètres

Dans cette étape, nous allons définir les paramètres nécessaires pour tracer les surfaces de décision sur l'ensemble de données iris.

```python
# Paramètres
n_classes = 3
n_estimators = 30
cmap = plt.cm.RdYlBu
plot_step = 0.02  # largeur d'étape fine pour les contours de la surface de décision
plot_step_coarser = 0.5  # largeurs d'étapes pour les prédictions grossières du classifieur
RANDOM_SEED = 13  # fixer la graine à chaque itération
```
