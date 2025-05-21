# Implementando a Inicialização Avançada na Estrutura

Acabamos de aprender duas técnicas poderosas para acessar argumentos de função. Agora, usaremos essas técnicas para atualizar nossa classe `Structure`. Primeiro, vamos entender por que estamos fazendo isso. Essas técnicas tornarão nossa classe mais flexível e fácil de usar, especialmente ao lidar com diferentes tipos de argumentos.

Abra o arquivo `structure.py` no editor de código. Você pode fazer isso executando os seguintes comandos no terminal. O comando `cd` altera o diretório para a pasta do projeto e o comando `code` abre o arquivo `structure.py` no editor de código.

```bash
cd ~/project
code structure.py
```

Substitua o conteúdo do arquivo pelo seguinte código. Este código define uma classe `Structure` com vários métodos. Vamos analisar cada parte para entender o que ela faz.

```python
import sys

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Get the caller's frame (the __init__ method that called this)
        frame = sys._getframe(1)

        # Get the local variables from that frame
        locs = frame.f_locals

        # Extract self and set other variables as attributes
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'{type(self).__name__!r} has no attribute {name!r}')
```

Aqui está o que fizemos no código:

1. Removemos o antigo método `__init__()`. Como as subclasses definirão seus próprios métodos `__init__`, não precisamos mais do antigo.
2. Adicionamos um novo método estático `_init()`. Este método usa a inspeção do frame para capturar e definir automaticamente todos os parâmetros como atributos. A inspeção do frame nos permite acessar as variáveis locais do método chamador.
3. Mantivemos o método `__repr__()`. Este método fornece uma boa representação de string do objeto, o que é útil para depuração e impressão.
4. Adicionamos um método `__setattr__()`. Este método impõe a validação de atributos, garantindo que apenas atributos válidos possam ser definidos no objeto.

Agora, vamos atualizar a classe `Stock`. Abra o arquivo `stock.py` usando o seguinte comando:

```bash
code stock.py
```

Substitua seu conteúdo pelo seguinte código:

```python
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()  # This magically captures and sets all parameters!

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

A principal mudança aqui é que nosso método `__init__` agora chama `self._init()` em vez de definir manualmente cada atributo. O método `_init()` usa a inspeção do frame para capturar e definir automaticamente todos os parâmetros como atributos. Isso torna o código mais conciso e fácil de manter.

Vamos testar nossa implementação executando os testes unitários. Os testes unitários nos ajudarão a garantir que nosso código funcione conforme o esperado. Execute os seguintes comandos no terminal:

```bash
cd ~/project
python3 teststock.py
```

Você deve ver que todos os testes passam, incluindo o teste para argumentos de palavra-chave que falhou antes. Isso significa que nossa implementação está funcionando corretamente.

Vamos também verificar a documentação de ajuda para nossa classe `Stock`. A documentação de ajuda fornece informações sobre a classe e seus métodos. Execute o seguinte comando no terminal:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Agora você deve ver uma assinatura adequada para o método `__init__`, mostrando todos os nomes dos parâmetros. Isso torna mais fácil para outros desenvolvedores entenderem como usar a classe.

Finalmente, vamos testar interativamente se os argumentos de palavra-chave funcionam conforme o esperado. Execute o seguinte comando no terminal:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

Você deve ver o objeto Stock criado corretamente com os atributos especificados. Isso confirma que nosso sistema de inicialização de classe suporta argumentos de palavra-chave.

Com esta implementação, alcançamos um sistema de inicialização de classe muito mais flexível e fácil de usar que:

1. Preserva as assinaturas de função adequadas na documentação, tornando mais fácil para os desenvolvedores entenderem como usar a classe.
2. Suporta argumentos posicionais e de palavra-chave, proporcionando mais flexibilidade ao criar objetos.
3. Requer um código boilerplate mínimo em subclasses, reduzindo a quantidade de código que você precisa escrever.
