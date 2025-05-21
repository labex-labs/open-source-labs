# Trabalhando com Listas Python

Listas são um tipo de estrutura de dados em Python. Uma estrutura de dados é uma maneira de organizar e armazenar dados para que possam ser usados eficientemente. Listas são muito versáteis porque podem armazenar diferentes tipos de itens, como números, strings ou até mesmo outras listas. Neste passo, aprenderemos como realizar várias operações em listas.

## Criando Listas a partir de Strings

Para começar a trabalhar com listas Python, primeiro precisamos abrir uma sessão interativa Python. Isso é como um ambiente especial onde podemos escrever e executar código Python imediatamente. Para iniciar esta sessão, digite o seguinte comando em seu terminal:

```bash
python3
```

Uma vez na sessão interativa Python, criaremos uma lista a partir de uma string. Uma string é apenas uma sequência de caracteres. Definiremos uma string que contém alguns símbolos de ações separados por espaços. Em seguida, converteremos essa string em uma lista. Cada símbolo de ação se tornará um elemento na lista.

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO GOOG'
>>> symlist = symbols.split()    # Dividir a string em espaços em branco
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG']
```

O método `split()` é usado para dividir a string em partes onde houver um espaço em branco. Cada parte então se torna um elemento na nova lista.

## Acessando e Modificando Elementos da Lista

Assim como as strings, as listas suportam indexação. Indexação significa que podemos acessar elementos individuais na lista por sua posição. Em Python, o primeiro elemento em uma lista tem um índice de 0, o segundo tem um índice de 1 e assim por diante. Também podemos usar indexação negativa para acessar elementos do final da lista. O último elemento tem um índice de -1, o penúltimo tem um índice de -2 e assim por diante.

Ao contrário das strings, os elementos da lista podem ser modificados. Isso significa que podemos alterar o valor de um elemento na lista.

```python
>>> symlist[0]    # Primeiro elemento
'HPQ'
>>> symlist[1]    # Segundo elemento
'AAPL'
>>> symlist[-1]   # Último elemento
'GOOG'
>>> symlist[-2]   # Penúltimo elemento
'YHOO'

>>> symlist[2] = 'AIG'    # Substituir o terceiro elemento
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
```

## Iterando Através de Listas

Frequentemente, precisamos realizar a mesma operação em cada elemento de uma lista. Podemos usar um loop `for` para fazer isso. Um loop `for` nos permite percorrer cada elemento da lista um por um e realizar uma ação específica nele.

```python
>>> for s in symlist:
...     print('s =', s)
...
```

Quando você executar este código, verá cada elemento da lista impresso com o rótulo `s =`.

```
s = HPQ
s = AAPL
s = AIG
s = MSFT
s = YHOO
s = GOOG
```

## Verificando a Pertinência

Às vezes, precisamos verificar se um determinado item existe em uma lista. Podemos usar o operador `in` para fazer isso. O operador `in` retorna `True` se o item estiver na lista e `False` caso contrário.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>> 'CAT' in symlist
False
```

## Adicionando e Removendo Elementos

Listas têm métodos embutidos que nos permitem adicionar e remover elementos. O método `append()` adiciona um elemento ao final da lista. O método `insert()` insere um elemento em uma posição específica na lista. O método `remove()` remove um elemento da lista por seu valor.

```python
>>> symlist.append('RHT')    # Adicionar um elemento ao final
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.insert(1, 'AA')    # Inserir em uma posição específica
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.remove('MSFT')    # Remover por valor
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

Se você tentar remover um elemento que não existe na lista, Python irá gerar um erro.

```python
>>> symlist.remove('MSFT')
```

Você verá uma mensagem de erro como esta:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

Também podemos encontrar a posição de um elemento na lista usando o método `index()`.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]    # Verificar o elemento nessa posição
'YHOO'
```

## Ordenando Listas

As listas podem ser ordenadas no local, o que significa que a lista original é modificada. Podemos ordenar uma lista alfabeticamente ou em ordem inversa.

```python
>>> symlist.sort()    # Ordenar alfabeticamente
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']

>>> symlist.sort(reverse=True)    # Ordenar em ordem inversa
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
```

## Listas Aninhadas

Listas podem conter qualquer tipo de objeto, incluindo outras listas. Isso é chamado de lista aninhada.

```python
>>> nums = [101, 102, 103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Para acessar elementos em uma lista aninhada, usamos vários índices. O primeiro índice seleciona o elemento da lista externa e o segundo índice seleciona o elemento da lista interna.

```python
>>> items[0]    # Primeiro elemento (o symlist)
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]    # Segundo elemento em symlist
'RHT'
>>> items[0][1][2]    # Terceiro caractere em 'RHT'
'T'
>>> items[1]    # Segundo elemento (a lista nums)
[101, 102, 103]
>>> items[1][1]    # Segundo elemento em nums
102
```

Quando terminar de trabalhar na sessão interativa Python, você pode sair digitando:

```python
>>> exit()
```
