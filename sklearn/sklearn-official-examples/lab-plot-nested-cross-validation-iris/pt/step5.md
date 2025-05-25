# Validação Cruzada Aninhada

Utilizamos validação cruzada aninhada para estimar o erro de generalização do modelo e seus hiperparâmetros. No loop interno, realizamos uma busca em grade para encontrar os melhores hiperparâmetros para cada conjunto de treinamento. No loop externo, avaliamos o desempenho do modelo no conjunto de teste.

```python
from sklearn.model_selection import KFold, cross_val_score

# Número de ensaios aleatórios
NUM_TRIALS = 30

# Arrays para armazenar as pontuações
non_nested_scores = np.zeros(NUM_TRIALS)
nested_scores = np.zeros(NUM_TRIALS)

# Loop para cada ensaio
for i in range(NUM_TRIALS):
    # Escolha de técnicas de validação cruzada para os loops interno e externo,
    # independentemente do conjunto de dados.
    inner_cv = KFold(n_splits=4, shuffle=True, random_state=i)
    outer_cv = KFold(n_splits=4, shuffle=True, random_state=i)

    # Validação cruzada aninhada com otimização de parâmetros
    clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=inner_cv)
    nested_score = cross_val_score(clf, X=X_iris, y=y_iris, cv=outer_cv)
    nested_scores[i] = nested_score.mean()

score_difference = non_nested_score - nested_scores.mean()
```
