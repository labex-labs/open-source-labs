# Escribiendo datos en un archivo Excel

También puedes escribir los datos en un archivo Excel utilizando el método `to_excel`. Guardemos nuestro DataFrame en un archivo Excel.

```python
# Guardando el DataFrame en un archivo Excel
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
```
