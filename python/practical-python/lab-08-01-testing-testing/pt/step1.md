# Asserções (Assertions)

A instrução `assert` é uma verificação interna para o programa. Se uma expressão não for verdadeira, ela levanta uma exceção `AssertionError`.

Sintaxe da instrução `assert`.

```python
assert <expression> [, 'Diagnostic message']
```

Por exemplo.

```python
assert isinstance(10, int), 'Expected int'
```

Ela não deve ser usada para verificar a entrada do usuário (ou seja, dados inseridos em um formulário web ou algo semelhante). Seu propósito é mais para verificações internas e invariantes (condições que sempre devem ser verdadeiras).
