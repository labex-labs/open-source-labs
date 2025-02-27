# Création de classifieurs

Nous allons créer des classifieurs MLP pour chaque valeur d'alpha. Nous allons créer un pipeline qui inclut StandardScaler pour standardiser les données et MLPClassifier avec différentes valeurs d'alpha. Nous allons définir le solveur sur 'lbfgs', qui est un optimiseur dans la famille des méthodes quasi-Newton. Nous allons définir max_iter sur 2000 et early_stopping sur True pour éviter le surapprentissage. Nous utiliserons deux couches cachées avec 10 neurones chacune.

```python
classifiers = []
names = []
for alpha in alphas:
    classifiers.append(
        make_pipeline(
            StandardScaler(),
            MLPClassifier(
                solver="lbfgs",
                alpha=alpha,
                random_state=1,
                max_iter=2000,
                early_stopping=True,
                hidden_layer_sizes=[10, 10],
            ),
        )
    )
    names.append(f"alpha {alpha:.2f}")
```
