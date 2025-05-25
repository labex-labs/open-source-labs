# Treinar e Avaliar o Modelo de Propagação de Rótulos

Nesta etapa, utilizaremos a Propagação de Rótulos (LabelSpreading) em 20% dos dados rotulados. Selecionaremos aleatoriamente 20% dos dados rotulados, treinaremos o modelo com esses dados e, em seguida, usaremos o modelo para prever os rótulos para os dados não rotulados restantes.

```python
# Treinar e avaliar o pipeline de Propagação de Rótulos
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "Pontuação F1 média no conjunto de teste: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
