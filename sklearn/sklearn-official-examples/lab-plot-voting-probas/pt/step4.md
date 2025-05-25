# Obter Probabilidades de Classe para a Primeira Amostra no Conjunto de Dados

Obteremos as probabilidades de classe para a primeira amostra no conjunto de dados e armazená-las em `class1_1` e `class2_1`.

```python
class1_1 = [pr[0, 0] for pr in probas]
class2_1 = [pr[0, 1] for pr in probas]
```
