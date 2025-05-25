# Avaliar o Pipeline

Agora, avaliaremos o pipeline no subconjunto de teste usando o método `predict`. O pipeline selecionará os 3 recursos mais informativos com base no valor F ANOVA, e a função `LinearSVC` fará previsões nos recursos selecionados.

```python
from sklearn.metrics import classification_report

y_pred = anova_svm.predict(X_test)
print(classification_report(y_test, y_pred))
```
