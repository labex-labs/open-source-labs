# Extraer subcadenas

Puedes extraer subcadenas utilizando expresiones regulares. El método `extract` acepta una expresión regular con al menos un grupo de captura.

```python
# extraer el primer dígito de cada cadena
s = pd.Series(["a1", "b2", "c3"], dtype="string")
s.str.extract(r"(\d)", expand=False)
```
