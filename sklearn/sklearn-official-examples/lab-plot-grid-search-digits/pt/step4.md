# Ajustar o Modelo e Fazer Previsões

Vamos ajustar o modelo e fazer previsões no conjunto de avaliação.

```python
grid_search.fit(X_train, y_train)

# Os parâmetros selecionados pela busca em grade com nossa estratégia personalizada são:
grid_search.best_params_

# Finalmente, avaliamos o modelo afinado no conjunto de avaliação deixado de fora: o
# objeto `grid_search` **foi automaticamente reapresentado** em todo o conjunto de treinamento
# com os parâmetros selecionados pela nossa estratégia de reapresentação personalizada.
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))
```
