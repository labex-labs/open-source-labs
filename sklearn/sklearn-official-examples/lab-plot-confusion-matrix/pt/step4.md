# Treinar Modelo

Treinaremos um classificador de máquina de vetores de suporte (SVM) usando um kernel linear. Usaremos um parâmetro de regularização C que é muito baixo para observar o impacto nos resultados.

```python
classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
```
