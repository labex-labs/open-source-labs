# Substituir Valores em uma Coluna

Finalmente, vamos substituir os valores na coluna `Sex`: 'male' por 'M' e 'female' por 'F'. Usaremos o método `replace()` para isso.

```python
# Substituir 'male' por 'M' e 'female' por 'F' na coluna 'Sex'
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
```
