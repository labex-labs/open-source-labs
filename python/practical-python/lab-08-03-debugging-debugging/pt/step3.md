# Usando o REPL

Use a opção `-i` para manter o Python ativo ao executar um script.

```bash
$ python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>>
```

Ele preserva o estado do interpretador. Isso significa que você pode investigar após a falha (_crash_), verificando os valores das variáveis e outros estados.
