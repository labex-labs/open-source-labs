# Exercício 7.10: Um decorador para medição de tempo

Se você define uma função, seu nome e módulo são armazenados nos atributos `__name__` e `__module__`. Por exemplo:

```python
>>> def add(x,y):
        return x+y

>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>>
```

Em um arquivo `timethis.py`, escreva uma função decoradora `timethis(func)` que envolve uma função com uma camada extra de lógica que imprime quanto tempo leva para uma função ser executada. Para fazer isso, você envolverá a função com chamadas de medição de tempo como esta:

```python
start = time.time()
r = func(*args,**kwargs)
end = time.time()
print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
```

Aqui está um exemplo de como seu decorador deve funcionar:

```python
>>> from timethis import timethis
>>> @timethis
def countdown(n):
    while n > 0:
        n -= 1

>>> countdown(10000000)
__main__.countdown : 0.076562
>>>
```

Discussão: Este decorador `@timethis` pode ser colocado na frente de qualquer definição de função. Assim, você pode usá-lo como uma ferramenta de diagnóstico para ajuste de desempenho.
