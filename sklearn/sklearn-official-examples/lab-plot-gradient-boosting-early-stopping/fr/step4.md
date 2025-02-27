# Construire et entraîner le modèle avec arrêt précoce

Nous allons maintenant construire et entraîner un modèle de gradient boosting avec arrêt précoce. Nous spécifions un _validation_fraction_ qui indique la fraction de l'ensemble de données complet qui sera mise de côté pour l'entraînement afin d'évaluer la perte de validation du modèle. Le modèle de gradient boosting est entraîné à l'aide de l'ensemble d'entraînement et évalué à l'aide de l'ensemble de validation. Lorsque chaque étape supplémentaire d'arbre de régression est ajoutée, l'ensemble de validation est utilisé pour évaluer le modèle. Cela se poursuit jusqu'à ce que les scores du modèle dans les dernières _n_iter_no_change_ étapes n'améliorent pas d'au moins _tol_. Après cela, le modèle est considéré comme convergé et l'ajout supplémentaire d'étapes est "arrêté tôt". Le nombre d'étapes du modèle final est disponible dans l'attribut _n_estimators_.

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
