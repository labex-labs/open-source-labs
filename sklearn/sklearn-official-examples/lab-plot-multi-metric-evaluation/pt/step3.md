# Definindo os hiperparâmetros e métricas de avaliação

Nesta etapa, definiremos os hiperparâmetros para o modelo `DecisionTreeClassifier` e as métricas de avaliação que usaremos. Usaremos as métricas AUC (Área Sob a Curva ROC) e Precisão.

```python
scoring = {"AUC": "roc_auc", "Accuracy": make_scorer(accuracy_score)}
```
