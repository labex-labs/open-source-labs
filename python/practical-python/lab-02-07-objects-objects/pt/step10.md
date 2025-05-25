# Tudo é um objeto

Números, strings, listas, funções, exceções, classes, instâncias, etc. são todos objetos. Isso significa que todos os objetos que podem ser nomeados podem ser passados como dados, colocados em contêineres, etc., sem quaisquer restrições. Não existem tipos _especiais_ de objetos. Às vezes, diz-se que todos os objetos são "first-class" (de primeira classe).

Um exemplo simples:

```python
>>> import math
>>> items = [abs, math, ValueError ]
>>> items
[<built-in function abs>,
  <module 'math' (builtin)>,
  <type 'exceptions.ValueError'>]
>>> items[0](-45)
45
>>> items[1].sqrt(2)
1.4142135623730951
>>> try:
        x = int('not a number')
    except items[2]:
        print('Failed!')
Failed!
>>>
```

Aqui, `items` é uma lista contendo uma função, um módulo e uma exceção. Você pode usar diretamente os itens na lista no lugar dos nomes originais:

```python
items[0](-45)       # abs
items[1].sqrt(2)    # math
except items[2]:    # ValueError
```

Com grande poder vem grande responsabilidade. Só porque você pode fazer isso não significa que você deva.

Neste conjunto de exercícios, analisamos um pouco do poder que vem dos objetos de primeira classe.
