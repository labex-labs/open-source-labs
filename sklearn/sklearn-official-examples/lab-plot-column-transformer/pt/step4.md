# Treinamento e Teste

Ajustaremos nosso pipeline aos dados de treinamento e o usaremos para prever tópicos para `X_test`. As métricas de desempenho do nosso pipeline são então impressas.

```python
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Relatório de classificação:\n\n{}".format(classification_report(y_test, y_pred)))
```
