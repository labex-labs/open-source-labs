# Exercício 3.8: Levantando exceções

A função `parse_csv()` que você escreveu na seção anterior permite que colunas especificadas pelo usuário sejam selecionadas, mas isso só funciona se o arquivo de dados de entrada tiver cabeçalhos de coluna.

Modifique o código para que uma exceção seja levantada se os argumentos `select` e `has_headers=False` forem passados. Por exemplo:

```python
>>> parse_csv('/home/labex/project/prices.csv', select=['name','price'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

Tendo adicionado essa verificação, você pode se perguntar se deveria estar realizando outros tipos de verificações de sanidade na função. Por exemplo, você deve verificar se o nome do arquivo é uma string, se `types` é uma lista, ou algo dessa natureza?

Como regra geral, geralmente é melhor pular esses testes e apenas deixar o programa falhar em entradas ruins. A mensagem de traceback apontará para a origem do problema e pode auxiliar na depuração.

A principal razão para adicionar a verificação acima é evitar a execução do código em um modo sem sentido (por exemplo, usando um recurso que requer cabeçalhos de coluna, mas simultaneamente especificando que não há cabeçalhos).

Isso indica um erro de programação por parte do código de chamada. Verificar casos que "não deveriam acontecer" é frequentemente uma boa ideia.
