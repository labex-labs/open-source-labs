# Leyendo datos desde un archivo Excel

Leer datos de un archivo Excel es tan fácil como leer datos de un archivo CSV. Utilizaremos la función `read_excel` de pandas.

```python
# Leyendo datos desde un archivo Excel
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```
