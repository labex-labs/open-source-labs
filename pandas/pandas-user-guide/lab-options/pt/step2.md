# Obtendo e Definindo Opções

Podemos obter ou definir o valor de uma única opção usando `pd.get_option` ou `pd.set_option`, respectivamente. Aqui, estamos definindo o número máximo de linhas a serem exibidas para 999.

```python
# Obter a configuração atual para o número máximo de linhas a serem exibidas
print(pd.options.display.max_rows)

# Definir o número máximo de linhas a serem exibidas para 999
pd.options.display.max_rows = 999

# Verificar a nova configuração
print(pd.options.display.max_rows)
```
