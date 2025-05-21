# Criando _Descriptors_ Personalizados

Nesta etapa, vamos criar nossa própria classe _descriptor_. Mas, primeiro, vamos entender o que é um _descriptor_. Um _descriptor_ é um objeto Python que implementa o protocolo de _descriptor_, que consiste nos métodos `__get__`, `__set__` e `__delete__`. Esses métodos permitem que o _descriptor_ gerencie como um atributo é acessado, definido e excluído. Ao criar nossa própria classe _descriptor_, podemos entender melhor como esse protocolo funciona.

Crie um novo arquivo chamado `descrip.py` no diretório do projeto. Este arquivo conterá nossa classe _descriptor_ personalizada. Aqui está o código:

```python
# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f'{self.name}:__get__')
        # In a real descriptor, you would return a value here

    def __set__(self, instance, value):
        print(f'{self.name}:__set__ {value}')
        # In a real descriptor, you would store the value here

    def __delete__(self, instance):
        print(f'{self.name}:__delete__')
        # In a real descriptor, you would delete the value here
```

Na classe `Descriptor`, o método `__init__` inicializa o _descriptor_ com um nome. O método `__get__` é chamado quando o atributo é acessado, o método `__set__` é chamado quando o atributo é definido e o método `__delete__` é chamado quando o atributo é excluído.

Agora, vamos criar um arquivo de teste para experimentar nosso _descriptor_ personalizado. Isso nos ajudará a ver como o _descriptor_ se comporta em diferentes cenários. Crie um arquivo chamado `test_descrip.py` com o seguinte código:

```python
# test_descrip.py

from descrip import Descriptor

class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

# Create an instance and try accessing the attributes
if __name__ == '__main__':
    f = Foo()
    print("Accessing attribute f.a:")
    f.a

    print("\nAccessing attribute f.b:")
    f.b

    print("\nSetting attribute f.a = 23:")
    f.a = 23

    print("\nDeleting attribute f.a:")
    del f.a
```

No arquivo `test_descrip.py`, importamos a classe `Descriptor` de `descrip.py`. Em seguida, criamos uma classe `Foo` com três atributos `a`, `b` e `c`, cada um gerenciado por um _descriptor_. Criamos uma instância de `Foo` e realizamos operações como acessar, definir e excluir atributos para ver como os métodos do _descriptor_ são chamados.

Agora, vamos executar este arquivo de teste para ver os _descriptors_ em ação. Abra seu terminal, navegue até o diretório do projeto e execute o arquivo de teste usando os seguintes comandos:

```bash
cd ~/project
python3 test_descrip.py
```

Você deve ver uma saída como esta:

```
Accessing attribute f.a:
a:__get__

Accessing attribute f.b:
b:__get__

Setting attribute f.a = 23:
a:__set__ 23

Deleting attribute f.a:
a:__delete__
```

Como você pode ver, toda vez que você acessa, define ou exclui um atributo que é gerenciado por um _descriptor_, o método mágico correspondente (`__get__`, `__set__` ou `__delete__`) é chamado.

Vamos também examinar nosso _descriptor_ interativamente. Isso nos permitirá testar o _descriptor_ em tempo real e ver os resultados imediatamente. Abra seu terminal, navegue até o diretório do projeto e inicie uma sessão Python interativa com o arquivo `descrip.py`:

```bash
cd ~/project
python3 -i descrip.py
```

Agora, digite estes comandos na sessão Python interativa para ver como o protocolo de _descriptor_ funciona:

```python
class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

f = Foo()
f.a         # Should call __get__
f.b         # Should call __get__
f.a = 23    # Should call __set__
del f.a     # Should call __delete__
exit()
```

A principal ideia aqui é que os _descriptors_ fornecem uma maneira de interceptar e personalizar o acesso a atributos. Isso os torna poderosos para implementar validação de dados, atributos computados e outros comportamentos avançados. Ao usar _descriptors_, você pode ter mais controle sobre como os atributos da sua classe são acessados, definidos e excluídos.
