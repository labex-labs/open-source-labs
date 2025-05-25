# Resetando Opções

Se desejamos redefinir uma ou mais opções para seus valores padrão, podemos usar `pd.reset_option`.

```python
# Redefinir o número máximo de linhas a serem exibidas para o padrão
pd.reset_option("display.max_rows")

# Verificar a redefinição
print(pd.options.display.max_rows)
```
