# Definir Classificadores e Parâmetros

Neste passo, definiremos os classificadores e os parâmetros a serem usados no processo de discretização de características. Criaremos uma lista de classificadores que inclui regressão logística, máquina de vetores de suporte linear (SVM), classificador de reforço de gradiente e SVM com um kernel de função de base radial. Também definiremos um conjunto de parâmetros para cada classificador a ser usado no algoritmo GridSearchCV.

```python
# lista de (estimador, param_grid), onde param_grid é usado em GridSearchCV
# Os espaços de parâmetros neste exemplo são limitados a uma faixa estreita para reduzir
# o seu tempo de execução. Em um caso de uso real, um espaço de busca mais amplo para os algoritmos
# deve ser usado.
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
