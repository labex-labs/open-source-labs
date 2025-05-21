# Criando Sua Primeira Metaclasse

Agora, vamos criar nossa primeira metaclasse. Antes de começarmos a codificar, vamos entender o que é uma metaclasse. Em Python, uma metaclasse é uma classe que cria outras classes. É como um modelo para classes. Quando você define uma classe em Python, o Python usa uma metaclasse para criar essa classe. Por padrão, o Python usa a metaclasse `type`. Nesta etapa, definiremos uma metaclasse personalizada que imprime informações sobre a classe que está criando. Isso nos ajudará a entender como as metaclasses funcionam por dentro.

1.  Abra o VSCode no WebIDE e crie um novo arquivo chamado `mymeta.py` no diretório `/home/labex/project`. É aqui que escreveremos nosso código para a metaclasse.

2.  Adicione o seguinte código ao arquivo:

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

Vamos detalhar o que esse código faz:

- Primeiro, definimos uma nova classe chamada `mytype` que herda de `type`. Como `type` é a metaclasse padrão em Python, ao herdar dela, estamos criando nossa própria metaclasse personalizada.
- Em seguida, substituímos o método `__new__`. Em Python, o método `__new__` é um método especial que é chamado ao criar um novo objeto. No contexto de uma metaclasse, ele é chamado ao criar uma nova classe.
- Dentro do nosso método `__new__`, imprimimos algumas informações sobre a classe que está sendo criada. Imprimimos o nome da classe, suas classes base e seus atributos. Depois disso, chamamos o método `__new__` do pai usando `super().__new__(meta, name, bases, __dict__)`. Isso é importante porque realmente cria a classe.
- Finalmente, criamos uma classe base chamada `myobject` e especificamos que ela deve usar nossa metaclasse personalizada `mytype`.

O método `__new__` recebe os seguintes parâmetros:

- `meta`: Isso se refere à própria metaclasse. Em nosso caso, é `mytype`.
- `name`: Este é o nome da classe que está sendo criada.
- `bases`: Esta é uma tupla contendo as classes base das quais a nova classe herda.
- `__dict__`: Este é um dicionário que contém os atributos da classe.

3.  Salve o arquivo pressionando Ctrl+S ou clicando em Arquivo > Salvar. Salvar o arquivo garante que seu código seja preservado e possa ser executado posteriormente.
