# Escrevendo Dados para o Excel

Você também pode escrever os dados para um arquivo Excel usando o método `to_excel`. Vamos salvar nosso DataFrame em um arquivo Excel.

```python
# Salvando o DataFrame em um arquivo Excel
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
```
