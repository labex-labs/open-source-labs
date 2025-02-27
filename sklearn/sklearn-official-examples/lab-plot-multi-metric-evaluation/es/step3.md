# Definir los hiperparámetros y las métricas de evaluación

En este paso, definiremos los hiperparámetros para el modelo DecisionTreeClassifier y las métricas de evaluación que utilizaremos. Utilizaremos las métricas AUC (Área Bajo la Curva) y Precisión.

```python
scoring = {"AUC": "roc_auc", "Accuracy": make_scorer(accuracy_score)}
```
