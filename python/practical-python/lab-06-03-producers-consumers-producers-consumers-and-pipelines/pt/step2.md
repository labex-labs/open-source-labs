# Pipelines de Geradores (Generator Pipelines)

Você pode usar este aspecto dos geradores para configurar pipelines de processamento (como pipes do Unix).

_produtor_ → _processamento_ → _processamento_ → _consumidor_

Pipes de processamento têm um produtor de dados inicial, um conjunto de estágios de processamento intermediários e um consumidor final.

**produtor** → _processamento_ → _processamento_ → _consumidor_

```python
def producer():
    ...
    yield item
    ...
```

O produtor é tipicamente um gerador. Embora também possa ser uma lista ou alguma outra sequência. `yield` alimenta dados no pipeline.

_produtor_ → _processamento_ → _processamento_ → **consumidor**

```python
def consumer(s):
    for item in s:
        ...
```

O consumidor é um loop for. Ele recebe itens e faz algo com eles.

_produtor_ → **processamento** → **processamento** → _consumidor_

```python
def processing(s):
    for item in s:
        ...
        yield newitem
        ...
```

Estágios de processamento intermediários consomem e produzem itens simultaneamente. Eles podem modificar o fluxo de dados. Eles também podem filtrar (descartando itens).

_produtor_ → _processamento_ → _processamento_ → _consumidor_

```python
def producer():
    ...
    yield item          # yields the item that is received by the `processing`
    ...

def processing(s):
    for item in s:      # Comes from the `producer`
        ...
        yield newitem   # yields a new item
        ...

def consumer(s):
    for item in s:      # Comes from the `processing`
        ...
```

Código para configurar o pipeline

```python
a = producer()
b = processing(a)
c = consumer(b)
```

Você notará que os dados fluem incrementalmente através das diferentes funções.

Para este exercício, o programa `stocksim.py` ainda deve estar rodando em segundo plano. Você vai usar a função `follow()` que você escreveu no exercício anterior.
