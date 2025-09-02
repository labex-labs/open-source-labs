# Criando um Decorador de Classe para Validação

Na etapa anterior, nossa implementação funcionou, mas havia uma redundância. Tivemos que especificar tanto a tupla `_fields` quanto os atributos descritores. Isso não é muito eficiente e podemos melhorar. Em Python, decoradores de classe são uma ferramenta poderosa que pode nos ajudar a simplificar esse processo. Um decorador de classe é uma função que recebe uma classe como argumento, a modifica de alguma forma e, em seguida, retorna a classe modificada. Ao usar um decorador de classe, podemos extrair automaticamente informações de campo dos descritores, o que tornará nosso código mais limpo e fácil de manter.

Vamos criar um decorador de classe para simplificar nosso código. Aqui estão os passos que você precisa seguir:

1. Primeiro, abra o arquivo `structure.py` no seu editor.

2. Em seguida, adicione o seguinte código no topo do arquivo `structure.py`, logo após quaisquer instruções de importação. Este código define nosso decorador de classe:

```python
from validate import Validator

def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields list automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

Vamos analisar o que este decorador faz:

- Ele primeiro cria uma lista vazia chamada `validators`. Em seguida, itera sobre todos os atributos da classe usando `vars(cls).items()`. Se um atributo for uma instância da classe `Validator`, ele adiciona esse atributo à lista `validators`.
- Depois disso, ele define o atributo `_fields` da classe. Ele cria uma lista de nomes a partir dos validadores na lista `validators` e a atribui a `cls._fields`.
- Finalmente, ele chama o método `create_init()` da classe para gerar o método `__init__` e, em seguida, retorna a classe modificada.

3. Assim que você adicionar o código, salve o arquivo `structure.py`. Salvar o arquivo garante que suas alterações sejam preservadas.

4. Agora, precisamos modificar nosso arquivo `stock.py` para usar este novo decorador. Abra o arquivo `stock.py` no seu editor.

5. Atualize o arquivo `stock.py` para usar o decorador `validate_attributes`. Substitua o código existente pelo seguinte:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Observe as mudanças que fizemos:

- Adicionamos o decorador `@validate_attributes` logo acima da definição da classe `Stock`. Isso informa ao Python para aplicar o decorador `validate_attributes` à classe `Stock`.
- Removemos a declaração explícita de `_fields` porque o decorador cuidará disso automaticamente.
- Também removemos a chamada para `Stock.create_init()` porque o decorador cuida da criação do método `__init__`.

Como resultado, a classe agora está mais simples e limpa. O decorador cuida de todos os detalhes que costumávamos lidar manualmente.

6. Após fazer essas alterações, precisamos verificar se tudo ainda funciona como esperado. Execute os testes novamente usando os seguintes comandos:

```bash
cd ~/project
python3 teststock.py
```

Se tudo estiver funcionando corretamente, você deverá ver a seguinte saída:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Esta saída indica que todos os testes foram concluídos com sucesso.

Vamos também testar nossa classe `Stock` interativamente. Execute o seguinte comando no terminal:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Você deverá ver a seguinte saída:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Ótimo! Você implementou com sucesso um decorador de classe que simplifica nosso código, cuidando automaticamente das declarações de campo e da inicialização. Isso torna nosso código mais eficiente e fácil de manter.
