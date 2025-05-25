# Ordenar Linhas da Tabela

Ordene o conjunto de dados Titanic de acordo com a idade dos passageiros e, em seguida, pela classe da cabine e idade em ordem decrescente.

```python
# Ordenar por Idade
titanic.sort_values(by="Age").head()

# Ordenar por Pclass e Idade em ordem decrescente
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
```
