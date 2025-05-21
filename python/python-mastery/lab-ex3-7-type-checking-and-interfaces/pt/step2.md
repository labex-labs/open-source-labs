# Implementando uma Classe Base Abstrata

Nesta etapa, vamos converter a classe `TableFormatter` em uma classe base abstrata (CBA) adequada usando o módulo `abc` do Python. Mas, primeiro, vamos entender o que é uma classe base abstrata e por que precisamos dela.

## Compreendendo as Classes Base Abstratas

Uma classe base abstrata é um tipo especial de classe em Python. É uma classe da qual você não pode criar um objeto diretamente, o que significa que você não pode instanciá-la. O principal objetivo de uma classe base abstrata é definir uma interface comum para suas subclasses. Ela define um conjunto de regras que todas as subclasses devem seguir. Especificamente, ela exige que as subclasses implementem certos métodos.

Aqui estão alguns conceitos-chave sobre classes base abstratas:

- Usamos o módulo `abc` em Python para criar classes base abstratas.
- Métodos marcados com o decorador `@abstractmethod` são como regras. Qualquer subclasse que herde de uma classe base abstrata deve implementar esses métodos.
- Se você tentar criar um objeto de uma classe que herda de uma classe base abstrata, mas não implementou todos os métodos necessários, o Python lançará um erro.

Agora que você entende o básico das classes base abstratas, vamos ver como podemos modificar a classe `TableFormatter` para se tornar uma.

## Modificando a Classe TableFormatter

Abra o arquivo `tableformat.py`. Vamos fazer algumas alterações na classe `TableFormatter` para que ela use o módulo `abc` e se torne uma classe base abstrata.

1. Primeiro, precisamos importar as coisas necessárias do módulo `abc`. Adicione a seguinte instrução de importação no topo do arquivo:

```python
# tableformat.py
from abc import ABC, abstractmethod
```

Esta instrução de importação traz duas coisas importantes: `ABC`, que é uma classe base para todas as classes base abstratas em Python, e `abstractmethod`, que é um decorador que usaremos para marcar métodos como abstratos.

2. Em seguida, modificaremos a classe `TableFormatter`. Ela deve herdar de `ABC` para se tornar uma classe base abstrata, e marcaremos seus métodos como abstratos usando o decorador `@abstractmethod`. Veja como a classe modificada deve ser:

```python
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        pass

    @abstractmethod
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        pass
```

Observe algumas coisas sobre esta classe modificada:

- A classe agora herda de `ABC`, o que significa que ela é oficialmente uma classe base abstrata.
- Os métodos `headings` e `row` são decorados com `@abstractmethod`. Isso informa ao Python que qualquer subclasse de `TableFormatter` deve implementar esses métodos.
- Substituímos o `NotImplementedError` por `pass`. O decorador `@abstractmethod` se encarrega de garantir que as subclasses implementem esses métodos, então não precisamos mais do `NotImplementedError`.

## Testando sua Classe Base Abstrata

Agora que tornamos a classe `TableFormatter` uma classe base abstrata, vamos testar se ela funciona corretamente. Criaremos um arquivo chamado `test_abc.py` com o seguinte código:

```python
from tableformat import TableFormatter

# Test case 1: Define a class with a misspelled method
try:
    class NewFormatter(TableFormatter):
        def headers(self, headings):  # Misspelled 'headings'
            pass
        def row(self, rowdata):
            pass

    f = NewFormatter()
    print("Test 1 failed - abstract method enforcement not working")
except TypeError as e:
    print(f"Test 1 passed - caught error: {e}")

# Test case 2: Define a class that properly implements all methods
try:
    class ProperFormatter(TableFormatter):
        def headings(self, headers):
            pass
        def row(self, rowdata):
            pass

    f = ProperFormatter()
    print("Test 2 passed - proper implementation works")
except TypeError as e:
    print(f"Test 2 failed - error: {e}")
```

Neste código, temos dois casos de teste. O primeiro caso de teste define uma classe `NewFormatter` que tenta herdar de `TableFormatter`, mas tem um nome de método com erro de ortografia. O segundo caso de teste define uma classe `ProperFormatter` que implementa corretamente todos os métodos necessários.

Para executar o teste, abra seu terminal e execute o seguinte comando:

```bash
python test_abc.py
```

Você deve ver uma saída semelhante a esta:

```
Test 1 passed - caught error: Can't instantiate abstract class NewFormatter with abstract methods headings
Test 2 passed - proper implementation works
```

Esta saída confirma que nossa classe base abstrata está funcionando como esperado. O primeiro caso de teste falha porque a classe `NewFormatter` não implementou o método `headings` corretamente. O segundo caso de teste passa porque a classe `ProperFormatter` implementou todos os métodos necessários.
