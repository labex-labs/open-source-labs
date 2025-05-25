# Exercício 6.8: Configurando um pipeline simples

Vamos ver a ideia de pipelining em ação. Escreva a seguinte função:

```python
>>> def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

>>>
```

Esta função é quase exatamente a mesma do primeiro exemplo de gerador no exercício anterior, exceto que ela não está mais abrindo um arquivo - ela simplesmente opera em uma sequência de linhas fornecidas como argumento. Agora, tente isto:

```python
>>> from follow import follow
>>> lines = follow('stocklog.csv')
>>> goog = filematch(lines, 'GOOG')
>>> for line in goog:
        print(line)

... aguarde a saída ...
```

Pode levar um tempo para a saída aparecer, mas eventualmente você deverá ver algumas linhas contendo dados para GOOG.

Nota: Estes exercícios devem ser realizados simultaneamente em dois terminais separados.
