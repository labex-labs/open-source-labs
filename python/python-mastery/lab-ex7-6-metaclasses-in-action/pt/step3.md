# Criando a Metaclasse StructureMeta

Agora, vamos falar sobre o que faremos a seguir. Encontramos uma maneira de coletar todos os tipos de validadores. Nossa próxima etapa é criar uma metaclasse. Mas o que exatamente é uma metaclasse? Em Python, uma metaclasse é um tipo especial de classe. Suas instâncias são as próprias classes. Isso significa que uma metaclasse pode controlar como uma classe é criada. Ela pode gerenciar o namespace onde os atributos da classe são definidos.

Em nossa situação, queremos criar uma metaclasse que tornará os tipos de validadores disponíveis quando definirmos uma subclasse `Structure`. Não queremos ter que importar esses tipos de validadores explicitamente toda vez.

Vamos começar abrindo o arquivo `structure.py` novamente. Você pode usar o seguinte comando para abri-lo:

```bash
code structure.py
```

Depois que o arquivo estiver aberto, precisamos adicionar algum código no topo, antes da definição da classe `Structure`. Este código definirá nossa metaclasse.

```python
from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        """Prepara o namespace para a classe que está sendo definida"""
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        """Cria a nova classe usando apenas o namespace local"""
        methods = methods.maps[0]  # Extrai o namespace local
        return super().__new__(meta, name, bases, methods)
```

Agora que definimos a metaclasse, precisamos modificar a classe `Structure` para usá-la. Dessa forma, qualquer classe que herde de `Structure` se beneficiará da funcionalidade da metaclasse.

```python
class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Esperava {len(self._fields)} argumentos')

        # Define todos os argumentos posicionais
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # Define os argumentos de palavra-chave restantes
        for name, val in kwargs.items():
            if name not in self._fields:
                raise TypeError(f'Argumento inválido: {name}')
            setattr(self, name, val)

    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        args_str = ','.join(repr(val) for val in values)
        return f'{type(self).__name__}({args_str})'
```

Vamos detalhar o que este código faz:

1. O método `__prepare__()` é um método especial em Python. Ele é chamado antes que a classe seja criada. Sua função é preparar o namespace onde os atributos da classe serão definidos. Usamos `ChainMap` aqui. `ChainMap` é uma ferramenta útil que cria um dicionário em camadas. Em nosso caso, ele inclui nossos tipos de validadores, tornando-os acessíveis no namespace da classe.

2. O método `__new__()` é responsável por criar a nova classe. Extraímos apenas o namespace local, que é o primeiro dicionário no `ChainMap`. Descartamos o dicionário de validadores porque já tornamos os tipos de validadores disponíveis no namespace.

Com esta configuração, qualquer classe que herde de `Structure` terá acesso a todos os tipos de validadores sem a necessidade de importá-los explicitamente.

Agora, vamos testar nossa implementação. Criaremos uma classe `Stock` usando nossa classe base `Structure` aprimorada.

```bash
cat > stock.py << EOF
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
EOF
```

Se nossa metaclasse estiver funcionando corretamente, devemos ser capazes de definir a classe `Stock` sem importar os tipos de validadores. Isso ocorre porque a metaclasse já os tornou disponíveis no namespace.
