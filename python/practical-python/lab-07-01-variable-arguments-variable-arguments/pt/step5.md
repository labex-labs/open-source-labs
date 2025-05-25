# Exercício 7.1: Um exemplo simples de argumentos variáveis

Tente definir a seguinte função:

```python
>>> def avg(x,*more):
        return float(x+sum(more))/(1+len(more))

>>> avg(10,11)
10.5
>>> avg(3,4,5)
4.0
>>> avg(1,2,3,4,5,6)
3.5
>>>
```

Note como o parâmetro `*more` coleta todos os argumentos extras.
