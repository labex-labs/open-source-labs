# Erros e Exceções

Funções relatam erros como exceções. Uma exceção faz com que uma função seja abortada e pode fazer com que todo o seu programa pare se não for tratada.

Tente isso no seu REPL Python.

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

Para fins de depuração, a mensagem descreve o que aconteceu, onde o erro ocorreu e um traceback mostrando as outras chamadas de função que levaram à falha.
