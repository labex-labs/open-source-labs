# Exercício 4.11: Definindo uma exceção personalizada

É frequentemente uma boa prática para bibliotecas definir suas próprias exceções.

Isso facilita a distinção entre exceções Python levantadas em resposta a erros comuns de programação versus exceções intencionalmente levantadas por uma biblioteca para sinalizar um problema específico de uso.

Modifique a função `create_formatter()` do exercício anterior para que ela levante uma exceção `FormatError` personalizada quando o usuário fornecer um nome de formato inválido.

Por exemplo:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('xls')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "tableformat.py", line 80, in create_formatter
    raise FormatError(f"Unknown table format {name}")
tableformat.FormatError: Unknown table format xls
>>>
```
