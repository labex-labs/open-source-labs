# Trabalhando com Strings Python

Strings são um dos tipos de dados mais comumente usados em Python. Elas são usadas para representar texto e podem conter letras, números e símbolos. Neste passo, exploraremos várias operações de string, que são habilidades essenciais para trabalhar com dados de texto em Python.

## Criando e Definindo Strings

Para começar a trabalhar com strings em Python, primeiro precisamos abrir um shell interativo Python. Este shell nos permite escrever e executar código Python linha por linha, o que é ótimo para aprender e testar. Abra um shell interativo Python novamente usando o seguinte comando:

```bash
python3
```

Uma vez que o shell esteja aberto, podemos definir uma string. Neste exemplo, criaremos uma string que contém símbolos de ações. Uma string em Python pode ser definida envolvendo texto entre aspas simples (`'`) ou aspas duplas (`"`). Veja como definimos nossa string:

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
>>> symbols
'AAPL IBM MSFT YHOO SCO'
```

Agora criamos uma variável de string chamada `symbols` e atribuímos um valor a ela. Quando digitamos o nome da variável e pressionamos Enter, Python exibe o valor da string.

## Acessando Caracteres e Substrings

Em Python, strings podem ser indexadas para acessar caracteres individuais. A indexação começa em 0, o que significa que o primeiro caractere de uma string tem um índice de 0, o segundo tem um índice de 1 e assim por diante. A indexação negativa também é suportada, onde -1 se refere ao último caractere, -2 se refere ao penúltimo caractere e assim por diante.

Vamos ver como podemos acessar caracteres individuais em nossa string `symbols`:

```python
>>> symbols[0]    # Primeiro caractere
'A'
>>> symbols[1]    # Segundo caractere
'A'
>>> symbols[2]    # Terceiro caractere
'P'
>>> symbols[-1]   # Último caractere
'O'
>>> symbols[-2]   # Penúltimo caractere
'C'
```

Também podemos extrair substrings usando fatiamento (slicing). O fatiamento nos permite obter uma parte da string especificando um índice inicial e final. A sintaxe para fatiamento é `string[start:end]`, onde a substring inclui caracteres do índice inicial até (mas não incluindo) o índice final.

```python
>>> symbols[:4]    # Primeiros 4 caracteres
'AAPL'
>>> symbols[-3:]   # Últimos 3 caracteres
'SCO'
>>> symbols[5:8]   # Caracteres do índice 5 a 7
'IBM'
```

## Imutabilidade de Strings

Strings em Python são imutáveis, o que significa que, uma vez que uma string é criada, você não pode alterar seus caracteres individuais. Se você tentar modificar um caractere em uma string, Python irá gerar um erro.

Vamos tentar alterar o primeiro caractere de nossa string `symbols`:

```python
>>> symbols[0] = 'a'    # Isso causará um erro
```

Você deve ver um erro como este:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Este erro indica que não podemos atribuir um novo valor a um caractere individual em uma string porque as strings são imutáveis.

## Concatenação de Strings

Embora não possamos modificar strings diretamente, podemos criar novas strings através da concatenação. Concatenação significa juntar duas ou mais strings. Em Python, podemos usar o operador `+` para concatenar strings.

```python
>>> symbols += ' GOOG'    # Anexar um novo símbolo
>>> symbols
'AAPL IBM MSFT YHOO SCO GOOG'

>>> symbols = 'HPQ ' + symbols    # Adicionar um novo símbolo no início
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

É importante lembrar que essas operações criam novas strings em vez de modificar a string original. A string original permanece inalterada, e uma nova string é criada com o valor combinado.

## Testando por Substrings

Para verificar se uma substring existe dentro de uma string, podemos usar o operador `in`. O operador `in` retorna `True` se a substring for encontrada na string e `False` caso contrário.

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
```

Observe que 'AA' retorna `True` porque é encontrado dentro de "AAPL". Esta é uma maneira útil de pesquisar texto específico dentro de uma string maior.

## Métodos de String

Strings Python vêm com inúmeros métodos embutidos que nos permitem realizar várias operações em strings. Esses métodos são funções que estão associadas ao objeto string e podem ser chamadas usando a notação de ponto (`string.method()`).

```python
>>> symbols.lower()    # Converter para minúsculas
'hpq aapl ibm msft yhoo sco goog'

>>> symbols    # A string original permanece inalterada
'HPQ AAPL IBM MSFT YHOO SCO GOOG'

>>> lowersyms = symbols.lower()    # Salvar o resultado em uma nova variável
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'

>>> symbols.find('MSFT')    # Encontrar o índice inicial de uma substring
13
>>> symbols[13:17]    # Verificar a substring nessa posição
'MSFT'

>>> symbols = symbols.replace('SCO','')    # Substituir uma substring
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
```

Quando terminar de experimentar, você pode sair do shell Python usando o seguinte comando:

```python
>>> exit()
```
