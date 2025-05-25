# Construir e Treinar o Modelo com Parada Antecipada

Agora, construiremos e treinaremos um modelo de boosting de gradientes com parada antecipada. Especificamos uma _fração de validação_, que representa a fração do conjunto de dados inteiro que será mantida separada do treinamento para avaliar a perda de validação do modelo. O modelo de boosting de gradientes é treinado usando o conjunto de treinamento e avaliado usando o conjunto de validação. Quando cada estágio adicional de árvore de regressão é adicionado, o conjunto de validação é usado para avaliar o modelo. Isso continua até que as pontuações do modelo nos últimos n_iter_no_change estágios não melhorem em pelo menos tol. Depois disso, o modelo é considerado convergido e a adição adicional de estágios é "parada antecipadamente". O número de estágios do modelo final está disponível no atributo n_estimators\*.

```python
gbes = ensemble.GradientBoostingClassifier(
        n_estimators=n_estimators,
        validation_fraction=0.2,
        n_iter_no_change=5,
        tol=0.01,
        random_state=0,
    )
start = time.time()
gbes.fit(X_train, y_train)
time_gbes.append(time.time() - start)
```
