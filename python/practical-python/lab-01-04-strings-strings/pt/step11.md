# f-Strings

Uma string com substituição de expressão formatada.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> a = f'{name:>10s} {shares:10d} {price:10.2f}'
>>> a
'       IBM        100      91.10'
>>> b = f'Cost = ${shares*price:0.2f}'
>>> b
'Cost = $9110.00'
>>>
```

**Nota:** Isso requer Python 3.6 ou mais recente. O significado dos códigos de formato será abordado mais tarde.

Nestes exercícios, você experimentará operações no tipo string do Python. Você deve fazer isso no prompt interativo do Python, onde pode ver facilmente os resultados. Nota importante:

> Em exercícios onde você deve interagir com o interpretador, `>>>` é o prompt do interpretador que você recebe quando o Python quer que você digite uma nova instrução. Algumas instruções no exercício abrangem várias linhas - para fazer essas instruções serem executadas, você pode ter que pressionar 'return' algumas vezes. Apenas um lembrete de que você _NÃO_ digita o `>>>` ao trabalhar com esses exemplos.

Comece definindo uma string contendo uma série de símbolos de ações como este:

```python
>>> symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
>>>
```
