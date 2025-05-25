# Capturando Todos os Erros (Catching All Errors)

Para capturar qualquer exceção, use `Exception` desta forma:

```python
try:
    ...
except Exception:       # DANGER. See below
    print('An error occurred')
```

Em geral, escrever código assim é uma má ideia porque você não terá ideia do porquê falhou.
