# Parâmetros Aninhados

Pode aceder aos parâmetros dos estimadores num pipeline usando a sintaxe `<estimador>__<parâmetro>`. Isto é útil para realizar buscas em grade sobre os parâmetros de todos os estimadores no pipeline. Aqui está um exemplo:

```python
pipe.set_params(clf__C=10)
```
