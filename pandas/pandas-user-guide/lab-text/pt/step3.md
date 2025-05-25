# Extraindo Substrings

Você pode extrair substrings usando expressões regulares. O método `extract` aceita uma expressão regular com pelo menos um grupo de captura.

```python
# extract the first digit from each string
s = pd.Series(["a1", "b2", "c3"], dtype="string")
s.str.extract(r"(\d)", expand=False)
```
