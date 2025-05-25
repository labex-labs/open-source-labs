# Strings Raw (Strings Brutas)

Strings raw (brutas) são literais de string com uma barra invertida não interpretada. Elas são especificadas prefixando a aspa inicial com um "r" minúsculo.

```python
>>> rs = r'c:\newdata\test' # Raw (uninterpreted backslash)
>>> rs
'c:\\newdata\\test'
```

A string é o texto literal contido dentro, exatamente como digitado. Isso é útil em situações onde a barra invertida tem um significado especial. Exemplo: nome de arquivo, expressões regulares, etc.
