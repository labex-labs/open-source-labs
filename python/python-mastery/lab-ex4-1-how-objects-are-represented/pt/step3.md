# Adicionando e Modificando Atributos de Objetos

Em Python, os objetos são implementados com base em dicionários. Essa implementação dá ao Python um alto grau de flexibilidade ao lidar com atributos de objetos. Ao contrário de algumas outras linguagens de programação, o Python não limita os atributos de um objeto apenas àqueles definidos em sua classe. Isso significa que você pode adicionar novos atributos a um objeto a qualquer momento, mesmo depois que o objeto foi criado.

Vamos explorar essa flexibilidade adicionando um novo atributo a uma de nossas instâncias. Suponha que tenhamos uma instância chamada `goog` de uma classe. Vamos adicionar um atributo `date` a ela:

```python
>>> goog.date = "6/11/2007"
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007'}
```

Aqui, adicionamos um novo atributo `date` à instância `goog`. Observe que esse atributo `date` não foi definido na classe `SimpleStock`. Esse novo atributo existe apenas na instância `goog`. Para confirmar isso, vamos verificar a instância `ibm`:

```python
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
>>> hasattr(ibm, 'date')
False
```

Como podemos ver, a instância `ibm` não possui o atributo `date`. Isso mostra três características importantes dos objetos Python:

1. Cada instância tem seu próprio conjunto exclusivo de atributos.
2. Os atributos podem ser adicionados a um objeto após sua criação.
3. Adicionar um atributo a uma instância não afeta outras instâncias.

Agora, vamos tentar uma maneira diferente de adicionar um atributo. Em vez de usar a notação de ponto, vamos manipular diretamente o dicionário subjacente do objeto. Em Python, cada objeto tem um atributo especial `__dict__` que armazena todos os seus atributos como pares chave-valor.

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007', 'time': '9:45am'}
```

Ao modificar diretamente o dicionário `__dict__`, adicionamos um novo atributo `time` à instância `goog`. Quando acessamos `goog.time`, o Python procura a chave 'time' no dicionário `__dict__` e retorna seu valor correspondente.

Esses exemplos ilustram que os objetos Python são essencialmente dicionários com alguns recursos extras. A flexibilidade dos objetos Python permite a modificação dinâmica, o que é muito poderoso e conveniente na programação.
