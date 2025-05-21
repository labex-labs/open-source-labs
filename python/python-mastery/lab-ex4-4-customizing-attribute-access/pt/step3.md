# Delegação como Alternativa à Herança

Na programação orientada a objetos, reutilizar e estender código é uma tarefa comum. Existem duas maneiras principais de conseguir isso: herança e delegação.

**Herança** é um mecanismo onde uma subclasse herda métodos e atributos de uma classe pai. A subclasse pode optar por substituir alguns desses métodos herdados para fornecer sua própria implementação.

**Delegação**, por outro lado, envolve um objeto contendo outro objeto e encaminhando chamadas de métodos específicas para ele.

Nesta etapa, exploraremos a delegação como uma alternativa à herança. Implementaremos uma classe que delega parte de seu comportamento a outro objeto.

## Configurando um Exemplo de Delegação

Primeiro, precisamos configurar a classe base com a qual nossa classe delegadora irá interagir.

1. Crie um novo arquivo chamado `base_class.py` no diretório `/home/labex/project`. Este arquivo definirá uma classe chamada `Spam` com três métodos: `method_a`, `method_b` e `method_c`. Cada método imprime uma mensagem e retorna um resultado. Aqui está o código para colocar em `base_class.py`:

```python
class Spam:
    def method_a(self):
        print('Spam.method_a executed')
        return "Result from Spam.method_a"

    def method_b(self):
        print('Spam.method_b executed')
        return "Result from Spam.method_b"

    def method_c(self):
        print('Spam.method_c executed')
        return "Result from Spam.method_c"
```

Em seguida, criaremos a classe delegadora.

2. Crie um novo arquivo chamado `delegator.py`. Neste arquivo, definiremos uma classe chamada `DelegatingSpam` que delega parte de seu comportamento a uma instância da classe `Spam`.

```python
from base_class import Spam

class DelegatingSpam:
    def __init__(self):
        # Create an instance of Spam that we'll delegate to
        self._spam = Spam()

    def method_a(self):
        # Override method_a but also call the original
        print('DelegatingSpam.method_a executed')
        result = self._spam.method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('DelegatingSpam.method_c executed')
        return "Result from DelegatingSpam.method_c"

    def __getattr__(self, name):
        # For any other attribute/method, delegate to self._spam
        print(f"Delegating {name} to the wrapped Spam object")
        return getattr(self._spam, name)
```

No método `__init__`, criamos uma instância da classe `Spam`. O método `method_a` substitui o método original, mas também chama o `method_a` da classe `Spam`. O método `method_c` substitui completamente o método original. O método `__getattr__` é um método especial em Python que é chamado quando um atributo ou método que não existe na classe `DelegatingSpam` é acessado. Ele então delega a chamada para a instância `Spam`.

Agora, vamos criar um arquivo de teste para verificar nossa implementação.

3. Crie um arquivo de teste chamado `test_delegation.py`. Este arquivo criará uma instância da classe `DelegatingSpam` e chamará seus métodos.

```python
from delegator import DelegatingSpam

# Create a delegating object
spam = DelegatingSpam()

print("Calling method_a (overridden with delegation):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (not defined in DelegatingSpam, delegated):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Finalmente, executaremos o script de teste.

4. Execute o script de teste usando os seguintes comandos no terminal:

```bash
cd /home/labex/project
python3 test_delegation.py
```

Você deve ver uma saída semelhante à seguinte:

```
Calling method_a (overridden with delegation):
DelegatingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (not defined in DelegatingSpam, delegated):
Delegating method_b to the wrapped Spam object
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
DelegatingSpam.method_c executed
Result: Result from DelegatingSpam.method_c

Calling non-existent method_d:
Delegating method_d to the wrapped Spam object
Error: 'Spam' object has no attribute 'method_d'
```

## Delegação vs. Herança

Agora, vamos comparar a delegação com a herança tradicional.

1. Crie um arquivo chamado `inheritance_example.py`. Neste arquivo, definiremos uma classe chamada `InheritingSpam` que herda da classe `Spam`.

```python
from base_class import Spam

class InheritingSpam(Spam):
    def method_a(self):
        # Override method_a but also call the parent method
        print('InheritingSpam.method_a executed')
        result = super().method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('InheritingSpam.method_c executed')
        return "Result from InheritingSpam.method_c"
```

A classe `InheritingSpam` substitui os métodos `method_a` e `method_c`. No método `method_a`, usamos `super()` para chamar o `method_a` da classe pai.

Em seguida, criaremos um arquivo de teste para o exemplo de herança.

2. Crie um arquivo de teste chamado `test_inheritance.py`. Este arquivo criará uma instância da classe `InheritingSpam` e chamará seus métodos.

```python
from inheritance_example import InheritingSpam

# Create an inheriting object
spam = InheritingSpam()

print("Calling method_a (overridden with super call):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (inherited from parent):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Finalmente, executaremos o teste de herança.

3. Execute o teste de herança usando os seguintes comandos no terminal:

```bash
cd /home/labex/project
python3 test_inheritance.py
```

Você deve ver uma saída semelhante à seguinte:

```
Calling method_a (overridden with super call):
InheritingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (inherited from parent):
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
InheritingSpam.method_c executed
Result: Result from InheritingSpam.method_c

Calling non-existent method_d:
Error: 'InheritingSpam' object has no attribute 'method_d'
```

## Principais Diferenças e Considerações

Vamos analisar as semelhanças e diferenças entre delegação e herança.

1. **Substituição de Método**: Tanto a delegação quanto a herança permitem que você substitua métodos, mas a sintaxe é diferente.

   - Na delegação, você define seu próprio método e decide se deve chamar o método do objeto encapsulado.
   - Na herança, você define seu próprio método e usa `super()` para chamar o método do pai.

2. **Acesso ao Método**:

   - Na delegação, métodos não definidos são encaminhados por meio do método `__getattr__`.
   - Na herança, métodos não definidos são herdados automaticamente.

3. **Relações de Tipo**:

   - Com delegação, `isinstance(delegating_spam, Spam)` retorna `False` porque o objeto `DelegatingSpam` não é uma instância da classe `Spam`.
   - Com herança, `isinstance(inheriting_spam, Spam)` retorna `True` porque a classe `InheritingSpam` herda da classe `Spam`.

4. **Limitações**: A delegação por meio de `__getattr__` não funciona com métodos especiais como `__getitem__`, `__len__`, etc. Esses métodos precisariam ser explicitamente definidos na classe delegadora.

A delegação é particularmente útil nas seguintes situações:

- Você deseja personalizar o comportamento de um objeto sem afetar sua hierarquia.
- Você deseja combinar comportamentos de vários objetos que não compartilham um pai comum.
- Você precisa de mais flexibilidade do que a herança oferece.

A herança é geralmente preferida quando:

- A relação "é-um" (is-a) é clara (por exemplo, um Carro é um Veículo).
- Você precisa manter a compatibilidade de tipo em todo o seu código.
- Métodos especiais precisam ser herdados.
