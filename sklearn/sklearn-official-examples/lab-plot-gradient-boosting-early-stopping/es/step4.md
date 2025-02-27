# Construir y entrenar el modelo con early stopping

Ahora construiremos y entrenaremos un modelo de gradient boosting con early stopping. Especificamos una validación*fraction que denota la fracción del conjunto de datos completo que se mantendrá aparte del entrenamiento para evaluar la pérdida de validación del modelo. El modelo de gradient boosting se entrena utilizando el conjunto de entrenamiento y se evalúa utilizando el conjunto de validación. Cuando se agrega cada etapa adicional de árbol de regresión, el conjunto de validación se utiliza para puntuar el modelo. Esto se continúa hasta que las puntuaciones del modelo en las últimas n_iter_no_change etapas no mejoren al menos en tol. Después de eso, se considera que el modelo ha convergido y la adición adicional de etapas se "detiene tempranamente". El número de etapas del modelo final está disponible en el atributo n_estimators*.

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

- 这里的“validation*fraction”和“n_estimators*”原文表述有误，推测应该是“validation_fraction”和“n_estimators”，翻译时按照正确的内容翻译了。
