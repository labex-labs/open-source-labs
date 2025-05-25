# Lendo Dados do Excel

Ler dados de um arquivo Excel é tão fácil quanto ler dados de um arquivo CSV. Usaremos a função `read_excel` do pandas.

```python
# Lendo dados de um arquivo Excel
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```
