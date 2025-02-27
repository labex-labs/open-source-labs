# Adjuntar el clasificador al flujo de preprocesamiento

En este paso, adjuntaremos el clasificador de regresión logística a nuestro flujo de preprocesamiento utilizando `Pipeline`.

```python
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
