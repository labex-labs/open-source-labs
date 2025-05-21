# Trabalhando com Dicionários Python

Em Python, dicionários são uma estrutura de dados fundamental. Eles são armazenamentos chave-valor (key-value), o que significa que permitem mapear um valor (o valor) para outro (a chave). Isso é extremamente útil ao lidar com dados que possuem relações naturais chave-valor. Por exemplo, você pode querer mapear o nome de uma pessoa (a chave) para sua idade (o valor), ou, como veremos neste laboratório, mapear símbolos de ações (chaves) para seus preços (valores).

## Criando e Acessando Dicionários

Vamos começar abrindo uma nova sessão interativa Python. Isso é como entrar em um ambiente especial onde você pode escrever e executar código Python linha por linha. Para iniciar esta sessão, abra seu terminal e digite o seguinte comando:

```bash
python3
```

Uma vez na sessão interativa Python, você pode criar um dicionário. Em nosso caso, criaremos um dicionário que mapeia símbolos de ações para seus preços. Veja como você faz isso:

```python
>>> prices = {'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
>>> prices
{'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
```

Na primeira linha, estamos criando um dicionário chamado `prices` e atribuindo a ele alguns pares chave-valor. As chaves são os símbolos das ações (`IBM`, `GOOG`, `AAPL`) e os valores são os preços correspondentes. A segunda linha apenas mostra o conteúdo do dicionário `prices`.

Agora, vamos ver como acessar e modificar os valores no dicionário usando as chaves.

```python
>>> prices['IBM']    # Acessar o valor para a chave 'IBM'
91.1

>>> prices['IBM'] = 123.45    # Atualizar um valor existente
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23}

>>> prices['HPQ'] = 26.15    # Adicionar um novo par chave-valor
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23, 'HPQ': 26.15}
```

Na primeira linha, estamos acessando o valor associado à chave `IBM`. Nas segunda e terceira linhas, estamos atualizando o valor da chave `IBM` e, em seguida, adicionando um novo par chave-valor (`HPQ` com um preço de `26.15`).

## Obtendo as Chaves do Dicionário

Às vezes, você pode querer obter uma lista de todas as chaves em um dicionário. Existem algumas maneiras de fazer isso.

```python
>>> list(prices)    # Converter as chaves do dicionário em uma lista
['IBM', 'GOOG', 'AAPL', 'HPQ']
```

Aqui, estamos usando a função `list()` para converter as chaves do dicionário `prices` em uma lista.

Você também pode usar o método `keys()`, que retorna um objeto especial chamado `dict_keys`.

```python
>>> prices.keys()    # Retorna um objeto dict_keys
dict_keys(['IBM', 'GOOG', 'AAPL', 'HPQ'])
```

## Obtendo os Valores do Dicionário

Da mesma forma, você pode querer obter todos os valores em um dicionário. Você pode usar o método `values()` para isso.

```python
>>> prices.values()    # Retorna um objeto dict_values
dict_values([123.45, 490.1, 312.23, 26.15])
```

Este método retorna um objeto `dict_values` que contém todos os valores no dicionário `prices`.

## Excluindo Itens

Se você deseja remover um par chave-valor de um dicionário, pode usar a palavra-chave `del`.

```python
>>> del prices['AAPL']    # Excluir a entrada 'AAPL'
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'HPQ': 26.15}
```

Aqui, estamos excluindo o par chave-valor com a chave `AAPL` do dicionário `prices`.

## Verificando se uma Chave Existe

Para verificar se uma chave existe em um dicionário, você pode usar o operador `in`.

```python
>>> 'IBM' in prices
True
>>> 'AAPL' in prices
False
```

O operador `in` retorna `True` se a chave existir no dicionário e `False` caso contrário.

## Métodos de Dicionário

Dicionários têm vários métodos úteis. Vamos analisar alguns deles.

```python
>>> prices.get('MSFT', 0)    # Obter valor ou padrão se a chave não existir
0
>>> prices.get('IBM', 0)
123.45

>>> prices.update({'MSFT': 25.0, 'GOOG': 500.0})    # Atualizar múltiplos valores
>>> prices
{'IBM': 123.45, 'GOOG': 500.0, 'HPQ': 26.15, 'MSFT': 25.0}
```

O método `get()` tenta obter o valor associado a uma chave. Se a chave não existir, ele retorna um valor padrão (neste caso, `0`). O método `update()` é usado para atualizar vários pares chave-valor no dicionário de uma só vez.

Quando terminar de trabalhar na sessão interativa Python, você pode sair digitando:

```python
>>> exit()
```
