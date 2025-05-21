# Compreendendo o Acesso a Atributos em Python

Em Python, objetos são um conceito fundamental. Eles podem armazenar dados em atributos, que são como contêineres nomeados para valores. Você pode pensar em atributos como variáveis que pertencem a um objeto. Existem várias maneiras de acessar esses atributos. O método mais direto e comumente usado é a notação de ponto (`.`). No entanto, Python também oferece funções específicas que lhe dão mais flexibilidade ao trabalhar com atributos.

## A Notação de Ponto

Vamos começar criando um objeto `Stock` e ver como podemos manipular seus atributos usando a notação de ponto. A notação de ponto é uma maneira simples e intuitiva de acessar e modificar os atributos de um objeto.

Primeiro, abra um novo terminal e inicie o shell interativo do Python. É aqui que você pode escrever e executar código Python linha por linha.

```python
# Abra um novo terminal e execute o shell interativo do Python
python3

# Importe a classe Stock do módulo stock
from stock import Stock

# Crie um objeto Stock
s = Stock('GOOG', 100, 490.1)

# Obtenha um atributo
print(s.name)    # Output: 'GOOG'

# Defina um atributo
s.shares = 50
print(s.shares)  # Output: 50

# Exclua um atributo
del s.shares
# Se tentarmos acessar s.shares agora, obteremos um AttributeError
```

No código acima, primeiro importamos a classe `Stock` do módulo `stock`. Em seguida, criamos uma instância da classe `Stock` chamada `s`. Para obter o valor do atributo `name`, usamos `s.name`. Para alterar o valor do atributo `shares`, simplesmente atribuímos um novo valor a `s.shares`. E se quisermos remover um atributo, usamos a palavra-chave `del` seguida pelo nome do atributo.

## Funções de Acesso a Atributos

Python fornece quatro funções embutidas que são muito úteis para a manipulação de atributos. Essas funções dão a você mais controle ao trabalhar com atributos, especialmente quando você precisa manipulá-los dinamicamente.

1. `getattr()` - Esta função é usada para obter o valor de um atributo.
2. `setattr()` - Permite definir o valor de um atributo.
3. `delattr()` - Você pode usar esta função para excluir um atributo.
4. `hasattr()` - Esta função verifica se um atributo existe em um objeto.

Vamos ver como usar essas funções:

```python
# Crie um novo objeto Stock
s = Stock('GOOG', 100, 490.1)

# Obtenha um atributo
print(getattr(s, 'name'))       # Output: 'GOOG'

# Defina um atributo
setattr(s, 'shares', 50)
print(s.shares)                 # Output: 50

# Verifique se um atributo existe
print(hasattr(s, 'name'))       # Output: True
print(hasattr(s, 'symbol'))     # Output: False

# Exclua um atributo
delattr(s, 'shares')
print(hasattr(s, 'shares'))     # Output: False
```

Essas funções são particularmente úteis quando você precisa trabalhar com atributos dinamicamente. Em vez de usar nomes de atributos codificados (hard-coded), você pode usar nomes de variáveis. Por exemplo, se você tiver uma variável que armazena o nome de um atributo, poderá passar essa variável para essas funções para realizar operações no atributo correspondente. Isso lhe dá mais flexibilidade em seu código, especialmente ao lidar com diferentes objetos e atributos de uma forma mais dinâmica.
