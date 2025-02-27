# Approximation du noyau à fonction de base radiale (RBF)

La classe RBFSampler implémente une mappage approximatif pour le noyau RBF, également connu sous le nom de Random Kitchen Sinks. Cette technique nous permet de modéliser explicitement une carte de noyau avant d'appliquer un algorithme linéaire, tel qu'un SVM linéaire ou une régression logistique.

Pour utiliser RBFSampler pour l'approximation de noyau, suivez ces étapes :

1. Initialisez l'objet RBFSampler avec la valeur souhaitée de gamma (le paramètre du noyau RBF) et le nombre de composants.

```python
from sklearn.kernel_approximation import RBFSampler

gamma = 0.1
n_components = 100
rbf_sampler = RBFSampler(gamma=gamma, n_components=n_components)
```

2. Ajustez l'objet RBFSampler aux données d'entraînement.

```python
rbf_sampler.fit(X_train)
```

3. Transformez vos données d'entraînement et de test à l'aide de l'objet RBFSampler.

```python
X_train_transformed = rbf_sampler.transform(X_train)
X_test_transformed = rbf_sampler.transform(X_test)
```
