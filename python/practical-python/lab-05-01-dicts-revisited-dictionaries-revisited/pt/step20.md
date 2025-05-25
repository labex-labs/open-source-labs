# Exercício 5.3: O papel das classes

As definições que compõem uma definição de classe são compartilhadas por todas as instâncias dessa classe. Observe que todas as instâncias têm um link de volta para sua classe associada:

```python
>>> goog.__class__
... veja a saída ...
>>> ibm.__class__
... veja a saída ...
>>>
```

Tente chamar um método nas instâncias:

```python
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
>>>
```

Observe que o nome 'cost' não está definido em `goog.__dict__` nem em `ibm.__dict__`. Em vez disso, ele está sendo fornecido pelo dicionário da classe. Tente isto:

```python
>>> Stock.__dict__['cost']
... veja a saída ...
>>>
```

Tente chamar o método `cost()` diretamente através do dicionário:

```python
>>> Stock.__dict__['cost'](goog)
49010.0
>>> Stock.__dict__['cost'](ibm)
4561.5
>>>
```

Observe como você está chamando a função definida na definição da classe e como o argumento `self` recebe a instância.

Tente adicionar um novo atributo à classe `Stock`:

```python
>>> Stock.foo = 42
>>>
```

Observe como este novo atributo agora aparece em todas as instâncias:

```python
>>> goog.foo
42
>>> ibm.foo
42
>>>
```

No entanto, observe que ele não faz parte do dicionário da instância:

```python
>>> goog.__dict__
... veja a saída e observe que não há atributo 'foo' ...
>>>
```

A razão pela qual você pode acessar o atributo `foo` nas instâncias é que o Python sempre verifica o dicionário da classe se não conseguir encontrar algo na própria instância.

Observação: Esta parte do exercício ilustra algo conhecido como variável de classe (class variable). Suponha, por exemplo, que você tenha uma classe como esta:

```python
class Foo(object):
     a = 13                  # Variável de classe (Class variable)
     def __init__(self,b):
         self.b = b          # Variável de instância (Instance variable)
```

Nesta classe, a variável `a`, atribuída no corpo da própria classe, é uma "variável de classe". Ela é compartilhada por todas as instâncias que são criadas. Por exemplo:

```python
>>> f = Foo(10)
>>> g = Foo(20)
>>> f.a          # Inspecione a variável de classe (a mesma para ambas as instâncias)
13
>>> g.a
13
>>> f.b          # Inspecione a variável de instância (difere)
10
>>> g.b
20
>>> Foo.a = 42   # Mude o valor da variável de classe
>>> f.a
42
>>> g.a
42
>>>
```
