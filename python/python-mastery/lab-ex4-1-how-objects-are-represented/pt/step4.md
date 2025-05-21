# Compreendendo a Relação entre Classes e Instâncias

Agora, vamos explorar como classes e instâncias se relacionam em Python e como a busca por métodos funciona. Este é um conceito importante porque ajuda você a entender como o Python encontra e usa métodos e atributos quando você trabalha com objetos.

Primeiro, vamos verificar a qual classe nossas instâncias pertencem. Conhecer a classe de uma instância é crucial, pois nos diz onde o Python procurará métodos e atributos relacionados a essa instância.

```python
>>> goog.__class__
<class '__main__.SimpleStock'>
>>> ibm.__class__
<class '__main__.SimpleStock'>
```

Ambas as instâncias têm uma referência de volta à classe `SimpleStock`. Essa referência é como um ponteiro que o Python usa quando precisa procurar métodos. Quando você chama um método em uma instância, o Python usa essa referência para encontrar a definição de método apropriada.

Quando você chama um método em uma instância, o Python segue estas etapas:

1. Ele procura o atributo no `__dict__` da instância. O `__dict__` de uma instância é como uma área de armazenamento onde todos os atributos específicos da instância são mantidos.
2. Se não for encontrado, ele verifica o `__dict__` da classe. O `__dict__` da classe armazena todos os atributos e métodos que são comuns a todas as instâncias dessa classe.
3. Se encontrado na classe, ele retorna esse atributo.

Vamos ver isso em ação. Primeiro, verifique se o método `cost` não está nos dicionários da instância. Essa etapa nos ajuda a entender que o método `cost` não é específico para cada instância, mas é definido no nível da classe.

```python
>>> 'cost' in goog.__dict__
False
>>> 'cost' in ibm.__dict__
False
```

Então, de onde vem o método `cost`? Vamos verificar a classe. Ao olhar para o `__dict__` da classe, podemos descobrir onde o método `cost` é definido.

```python
>>> SimpleStock.__dict__['cost']
<function SimpleStock.cost at 0x7f...>
```

O método é definido na classe, não nas instâncias. Quando você chama `goog.cost()`, o Python não encontra `cost` em `goog.__dict__`, então ele procura em `SimpleStock.__dict__` e o encontra lá.

Você pode realmente chamar o método diretamente do dicionário da classe, passando a instância como o primeiro argumento (que se torna `self`). Isso mostra como o Python internamente chama métodos quando você usa a sintaxe normal instance.method().

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.0
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
```

Isso é essencialmente o que o Python faz nos bastidores quando você chama `goog.cost()`.

Agora, vamos adicionar um atributo de classe. Atributos de classe são compartilhados por todas as instâncias. Isso significa que todas as instâncias da classe podem acessar esse atributo, e ele é armazenado apenas uma vez no nível da classe.

```python
>>> SimpleStock.exchange = 'NASDAQ'
>>> goog.exchange
'NASDAQ'
>>> ibm.exchange
'NASDAQ'
```

Ambas as instâncias podem acessar o atributo `exchange`, mas ele não é armazenado em seus dicionários individuais. Vamos verificar isso verificando os dicionários de instância e classe.

```python
>>> 'exchange' in goog.__dict__
False
>>> 'exchange' in SimpleStock.__dict__
True
>>> SimpleStock.__dict__['exchange']
'NASDAQ'
```

Isso demonstra que:

1. Os atributos de classe são compartilhados por todas as instâncias. Todas as instâncias podem acessar o mesmo atributo de classe sem ter sua própria cópia.
2. O Python verifica o dicionário da instância primeiro, depois o dicionário da classe. Essa é a ordem em que o Python procura atributos quando você tenta acessá-los em uma instância.
3. As classes atuam como um repositório para dados e comportamentos compartilhados (métodos). A classe armazena todos os atributos e métodos comuns que podem ser usados por todas as suas instâncias.

Se modificarmos um atributo de instância com o mesmo nome, ele sombreia o atributo de classe. Isso significa que, quando você acessa o atributo nessa instância, o Python usará o valor específico da instância em vez do valor no nível da classe.

```python
>>> ibm.exchange = 'NYSE'
>>> ibm.exchange
'NYSE'
>>> goog.exchange  # Ainda usando o atributo da classe
'NASDAQ'
>>> ibm.__dict__['exchange']
'NYSE'
```

Agora, `ibm` tem seu próprio atributo `exchange` que sombreia o atributo da classe, enquanto `goog` ainda usa o atributo da classe.
