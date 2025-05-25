# Avaliação

Nesta etapa, avaliamos o desempenho do modelo no conjunto de dados de teste. Usamos a função `classification_report` do módulo `sklearn.metrics` para gerar o relatório de classificação tanto para o modelo de pipeline quanto para o modelo de regressão logística.

```python
from sklearn import metrics

Y_pred = rbm_features_classifier.predict(X_test)
print(
    "Regressão logística usando características RBM:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)

# Treinando o classificador de regressão logística diretamente nas pixels
raw_pixel_classifier = clone(logistic)
raw_pixel_classifier.C = 100.0
raw_pixel_classifier.fit(X_train, Y_train)

Y_pred = raw_pixel_classifier.predict(X_test)
print(
    "Regressão logística usando características de pixel bruto:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)
```
