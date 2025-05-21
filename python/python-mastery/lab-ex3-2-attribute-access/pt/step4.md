# Compreendendo Métodos Vinculados em Python

Em Python, métodos são um tipo especial de atributos que você pode chamar. Quando você acessa um método através de um objeto, você está obtendo o que chamamos de "método vinculado" (bound method). Um método vinculado é essencialmente um método que está ligado a um objeto específico. Isso significa que ele tem acesso aos dados do objeto e pode operar sobre eles.

## Acessando Métodos como Atributos

Vamos começar a explorar métodos vinculados usando nossa classe `Stock`. Primeiro, veremos como acessar um método como um atributo de um objeto.

```python
# Abra um shell interativo do Python
python3

# Importe a classe Stock e crie um objeto stock
from stock import Stock
s = Stock('GOOG', 100, 490.10)

# Acesse o método cost sem chamá-lo
cost_method = s.cost
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Chame o método
result = cost_method()
print(result)  # Output: 49010.0

# Você também pode fazer isso em uma etapa
print(s.cost())  # Output: 49010.0
```

No código acima, primeiro importamos a classe `Stock` e criamos uma instância dela. Em seguida, acessamos o método `cost` do objeto `s` sem realmente chamá-lo. Isso nos dá um método vinculado. Quando chamamos este método vinculado, ele calcula o custo com base nos dados do objeto. Você também pode chamar diretamente o método no objeto em uma etapa.

## Usando getattr() com Métodos

Outra maneira de acessar métodos é usando a função `getattr()`. Esta função permite que você obtenha um atributo de um objeto por seu nome.

```python
# Obtenha o método cost usando getattr
cost_method = getattr(s, 'cost')
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Chame o método
result = cost_method()
print(result)  # Output: 49010.0

# Obtenha e chame em uma etapa
result = getattr(s, 'cost')()
print(result)  # Output: 49010.0
```

Aqui, usamos `getattr()` para obter o método `cost` do objeto `s`. Assim como antes, podemos chamar o método vinculado para obter o resultado. E você pode até obter e chamar o método em uma única linha.

## O Método Vinculado e Seu Objeto

Um método vinculado sempre mantém uma referência ao objeto do qual foi acessado. Isso significa que, mesmo que você armazene o método em uma variável, ele ainda sabe a qual objeto pertence e pode acessar os dados do objeto.

```python
# Armazene o método cost em uma variável
c = s.cost

# Chame o método
print(c())  # Output: 49010.0

# Altere o estado do objeto
s.shares = 75

# Chame o método novamente - ele vê o estado atualizado
print(c())  # Output: 36757.5
```

Neste exemplo, armazenamos o método `cost` em uma variável `c`. Quando chamamos `c()`, ele calcula o custo com base nos dados atuais do objeto. Em seguida, alteramos o atributo `shares` do objeto `s`. Quando chamamos `c()` novamente, ele usa os dados atualizados para calcular o novo custo.

## Explorando os Interiores do Método Vinculado

Um método vinculado tem dois atributos importantes que nos dão mais informações sobre ele.

- `__self__`: Este atributo se refere ao objeto ao qual o método está vinculado.
- `__func__`: Este atributo é o objeto de função real que representa o método.

```python
# Obtenha o método cost
c = s.cost

# Examine os atributos do método vinculado
print(c.__self__)  # Output: <stock.Stock object at 0x...>
print(c.__func__)  # Output: <function Stock.cost at 0x...>

# Você pode chamar manualmente a função com o objeto
print(c.__func__(c.__self__))  # Output: 36757.5 (same as c())
```

Aqui, acessamos os atributos `__self__` e `__func__` do método vinculado `c`. Podemos ver que `__self__` é o objeto `s`, e `__func__` é a função `cost`. Podemos até mesmo chamar manualmente a função passando o objeto como um argumento, e isso nos dá o mesmo resultado que chamar o método vinculado diretamente.

## Exemplo com um Método que Aceita Argumentos

Vamos ver como os métodos vinculados funcionam com um método que aceita argumentos, como o método `sell()`.

```python
# Obtenha o método sell
sell_method = s.sell

# Examine o método
print(sell_method)  # Output: <bound method Stock.sell of <stock.Stock object at 0x...>>

# Chame o método com um argumento
sell_method(25)
print(s.shares)  # Output: 50

# Chame o método manualmente usando __func__ e __self__
sell_method.__func__(sell_method.__self__, 10)
print(s.shares)  # Output: 40
```

Neste exemplo, obtemos o método `sell` como um método vinculado. Quando o chamamos com um argumento, ele atualiza o atributo `shares` do objeto `s`. Também podemos chamar manualmente o método usando os atributos `__func__` e `__self__`, passando o argumento também.

Compreender os métodos vinculados ajuda você a compreender como o sistema de objetos do Python funciona por dentro, o que pode ser útil para depuração, metaprogramação e criação de padrões de programação avançados.
