# Добавление классификатора в конвейер предварительной обработки

В этом шаге мы добавим классификатор логистической регрессии в наш конвейер предварительной обработки с использованием `Pipeline`.

```python
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
