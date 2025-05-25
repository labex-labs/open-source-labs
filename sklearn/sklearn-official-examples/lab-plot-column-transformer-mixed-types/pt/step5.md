# Adicionar o Classificador ao Pipeline de Pré-processamento

Neste passo, adicionaremos o classificador de regressão logística ao nosso pipeline de pré-processamento utilizando `Pipeline`.

```python
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
