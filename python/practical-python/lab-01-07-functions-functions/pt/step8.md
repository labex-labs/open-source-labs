# Exercício 1.31: Tratamento de erros

O que acontece se você tentar sua função em um arquivo com alguns campos ausentes?

```python
>>> portfolio_cost('missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "pcost.py", line 11, in portfolio_cost
    nshares    = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

Neste ponto, você se depara com uma decisão. Para fazer o programa funcionar, você pode ou sanitizar o arquivo de entrada original, eliminando as linhas ruins, ou pode modificar seu código para lidar com as linhas ruins de alguma forma.

Modifique o programa `pcost.py` para capturar a exceção, imprimir uma mensagem de aviso e continuar processando o restante do arquivo.
