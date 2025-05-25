# Usando option_context

A função `option_context` nos permite executar um bloco de código com um conjunto de opções que revertem para as configurações anteriores após a execução.

```python
# Executar um bloco de código com um conjunto de opções
with pd.option_context("display.max_rows", 10):
    # Isso imprimirá 10, apesar da configuração global ser diferente
    print(pd.get_option("display.max_rows"))

# Isso imprimirá a configuração global, pois o bloco de contexto terminou
print(pd.get_option("display.max_rows"))
```
