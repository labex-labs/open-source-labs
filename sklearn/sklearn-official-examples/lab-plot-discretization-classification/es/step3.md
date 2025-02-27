# Definir clasificadores y parámetros

En este paso, definiremos los clasificadores y parámetros que se utilizarán en el proceso de discretización de características. Crearemos una lista de clasificadores que incluye regresión logística, máquina de vectores de soporte lineal (SVM), clasificador de aumento de gradiente y SVM con un kernel de función de base radial. También definiremos un conjunto de parámetros para cada clasificador que se utilizarán en el algoritmo GridSearchCV.

```python
# lista de (estimador, param_grid), donde param_grid se utiliza en GridSearchCV
# Los espacios de parámetros en este ejemplo se limitan a una banda estrecha para reducir
# su tiempo de ejecución. En un caso de uso real, se debería utilizar un espacio de búsqueda más amplio para los algoritmos.
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
