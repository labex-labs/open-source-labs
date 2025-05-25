# Treinar o Pipeline

Agora, treinaremos o pipeline no subconjunto de treinamento usando o método `fit`. Durante o treinamento, a função `SelectKBest` selecionará os 3 recursos mais informativos com base no valor F ANOVA, e a função `LinearSVC` treinará um classificador SVM linear nos recursos selecionados.

```python
anova_svm.fit(X_train, y_train)
```
