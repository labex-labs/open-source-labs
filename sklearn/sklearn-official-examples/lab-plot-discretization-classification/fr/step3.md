# Définir les classifieurs et les paramètres

Dans cette étape, nous allons définir les classifieurs et les paramètres à utiliser dans le processus de discrétisation des fonctionnalités. Nous allons créer une liste de classifieurs qui inclut la régression logistique, la machine à vecteurs de support linéaire (SVM), le classifieur à gradient boosting et la SVM avec un noyau de fonction de base radiale. Nous allons également définir un ensemble de paramètres pour chaque classifieur à utiliser dans l'algorithme GridSearchCV.

```python
# liste de (estimateur, param_grid), où param_grid est utilisé dans GridSearchCV
# Les espaces de paramètres dans cet exemple sont limités à une bande étroite pour réduire
# son temps d'exécution. Dans un cas d'utilisation réel, un espace de recherche plus large pour les algorithmes
# devrait être utilisé.
classifiers = [
    (
        make_pipeline(StandardScaler(), LogisticRegression(random_state=0)),
        {"logisticregression__C": np.logspace(-1, 1, 3)},
    ),
    (
        make_pipeline(StandardScaler(), LinearSVC(random_state=0, dual="auto")),
        {"linearsvc__C": np.logspace(-1, 1, 3)},
    ),
    (
        make_pipeline(
            StandardScaler(),
            KBinsDiscretizer(encode="onehot"),
            LogisticRegression(random_state=0),
        ),
        {
            "kbinsdiscretizer__n_bins": np.arange(5, 8),
            "logisticregression__C": np.logspace(-1, 1, 3),
        },
    ),
    (
        make_pipeline(
            StandardScaler(),
            KBinsDiscretizer(encode="onehot"),
            LinearSVC(random_state=0, dual="auto"),
        ),
        {
            "kbinsdiscretizer__n_bins": np.arange(5, 8),
            "linearsvc__C": np.logspace(-1, 1, 3),
        },
    ),
    (
        make_pipeline(
            StandardScaler(), GradientBoostingClassifier(n_estimators=5, random_state=0)
        ),
        {"gradientboostingclassifier__learning_rate": np.logspace(-2, 0, 5)},
    ),
    (
        make_pipeline(StandardScaler(), SVC(random_state=0)),
        {"svc__C": np.logspace(-1, 1, 3)},
    ),
]

names = [get_name(e).replace("StandardScaler + ", "") for e, _ in classifiers]
```
