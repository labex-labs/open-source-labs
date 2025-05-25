# Exercício 5.2: Modificação de Dados da Instância

Tente definir um novo atributo em uma das instâncias acima:

```python
>>> goog.date = '6/11/2007'
>>> goog.__dict__
... veja a saída ...
>>> ibm.__dict__
... veja a saída ...
>>>
```

Na saída acima, você notará que a instância `goog` tem um atributo `date`, enquanto a instância `ibm` não tem. É importante notar que o Python realmente não impõe nenhuma restrição aos atributos. Por exemplo, os atributos de uma instância não se limitam àqueles configurados no método `__init__()`.

Em vez de definir um atributo, tente colocar um novo valor diretamente no objeto `__dict__`:

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>>
```

Aqui, você realmente percebe o fato de que uma instância é apenas uma camada sobre um dicionário. Observação: deve-se enfatizar que a manipulação direta do dicionário é incomum - você sempre deve escrever seu código para usar a sintaxe (.).
