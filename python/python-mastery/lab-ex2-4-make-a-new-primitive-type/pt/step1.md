# Criando uma Classe `MutInt` Básica

Vamos começar criando uma classe básica para o nosso tipo Inteiro Mutável. Em programação, uma classe é como um projeto para criar objetos. Nesta etapa, criaremos a base do nosso novo tipo primitivo. Um tipo primitivo é um tipo de dado básico fornecido por uma linguagem de programação, e aqui vamos construir o nosso próprio personalizado.

1. Abra o WebIDE e navegue até o diretório `/home/labex/project`. O WebIDE é um ambiente de desenvolvimento integrado onde você pode escrever, editar e executar seu código. Navegar para este diretório garante que todos os seus arquivos sejam organizados em um só lugar e possam interagir uns com os outros corretamente.

2. Abra o arquivo `mutint.py` que foi criado para você na etapa de configuração. Este arquivo será o lar da nossa definição de classe `MutInt`.

3. Adicione o seguinte código para definir uma classe `MutInt` básica:

```python
# mutint.py

class MutInt:
    """
    Uma classe de inteiro mutável que permite que seu valor seja modificado após a criação.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Inicializa com um valor inteiro."""
        self.value = value
```

O atributo `__slots__` é usado para definir os atributos que esta classe pode ter. Atributos são como variáveis que pertencem a um objeto da classe. Ao usar `__slots__`, dizemos ao Python para usar uma maneira mais eficiente em termos de memória para armazenar atributos. Neste caso, nossa classe `MutInt` terá apenas um único atributo chamado `value`. Isso significa que cada objeto da classe `MutInt` só poderá conter um pedaço de dados, que é o valor inteiro.

O método `__init__` é o construtor para nossa classe. Um construtor é um método especial que é chamado quando um objeto da classe é criado. Ele recebe um parâmetro de valor e o armazena no atributo `value` da instância. Uma instância é um objeto individual criado a partir do projeto da classe.

Vamos testar nossa classe criando um script Python para usá-la:

4. Crie um novo arquivo chamado `test_mutint.py` no mesmo diretório:

```python
# test_mutint.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)
print(f"Created MutInt with value: {a.value}")

# Modify the value (demonstrating mutability)
a.value = 42
print(f"Modified value to: {a.value}")

# Try adding (this will fail)
try:
    result = a + 10
    print(f"Result of a + 10: {result}")
except TypeError as e:
    print(f"Error when adding: {e}")
```

Neste script de teste, primeiro importamos a classe `MutInt` do arquivo `mutint.py`. Em seguida, criamos um objeto da classe `MutInt` com um valor inicial de 3. Imprimimos o valor inicial, depois o modificamos para 42 e imprimimos o novo valor. Finalmente, tentamos adicionar 10 ao objeto `MutInt`, o que resultará em um erro porque nossa classe ainda não suporta a operação de adição.

5. Execute o script de teste executando o seguinte comando no terminal:

```bash
python3 /home/labex/project/test_mutint.py
```

O terminal é uma interface de linha de comando onde você pode executar vários comandos para interagir com seu sistema e seu código. Executar este comando executará o script `test_mutint.py`.

Você deve ver uma saída semelhante a esta:

```
Created MutInt with value: 3
Modified value to: 42
Error when adding: unsupported operand type(s) for +: 'MutInt' and 'int'
```

Nossa classe `MutInt` armazena e atualiza um valor com sucesso. No entanto, ela tem várias limitações:

- Não é exibida de forma agradável quando impressa
- Não suporta operações matemáticas como adição
- Não suporta comparações
- Não suporta conversões de tipo

Nas próximas etapas, abordaremos essas limitações uma por uma para fazer com que nossa classe `MutInt` se comporte mais como um verdadeiro tipo primitivo.
