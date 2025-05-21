# Compreendendo as Classes Validadoras

Neste laboratório, vamos construir um conjunto de classes validadoras para criar um objeto chamável. Antes de começarmos a construir, é importante entender as classes validadoras fornecidas no arquivo `validate.py`. Essas classes nos ajudarão a realizar a verificação de tipo (type checking), que é uma parte crucial para garantir que nosso código funcione como esperado.

Vamos começar abrindo o arquivo `validate.py` no WebIDE. Este arquivo contém o código para as classes validadoras que usaremos. Para abri-lo, execute o seguinte comando no terminal:

```bash
code /home/labex/project/validate.py
```

Depois de abrir o arquivo, você verá que ele contém várias classes. Aqui está uma breve visão geral do que cada classe faz:

1. `Validator`: Esta é uma classe base. Ela tem um método `check`, mas atualmente, este método não faz nada. Ele serve como um ponto de partida para as outras classes validadoras.
2. `Typed`: Esta é uma subclasse de `Validator`. Sua principal função é verificar se um valor é de um tipo específico.
3. `Integer`, `Float` e `String`: Estes são validadores de tipo específicos que herdam de `Typed`. Eles são projetados para verificar se um valor é um inteiro, um float ou uma string, respectivamente.

Agora, vamos ver como essas classes validadoras funcionam na prática. Criaremos um novo arquivo chamado `test.py` para testá-las. Para criar e abrir este arquivo, execute o seguinte comando:

```bash
code /home/labex/project/test.py
```

Depois que o arquivo `test.py` estiver aberto, adicione o seguinte código a ele. Este código testará os validadores `Integer` e `String`:

```python
from validate import Integer, String, Float

# Test Integer validator
print("Testing Integer validator:")
try:
    Integer.check(42)
    print("✓ Integer check passed for 42")
except TypeError as e:
    print(f"✗ Error: {e}")

try:
    Integer.check("Hello")
    print("✗ Integer check incorrectly passed for 'Hello'")
except TypeError as e:
    print(f"✓ Correctly raised error: {e}")

# Test String validator
print("\nTesting String validator:")
try:
    String.check("Hello")
    print("✓ String check passed for 'Hello'")
except TypeError as e:
    print(f"✗ Error: {e}")
```

Neste código, primeiro importamos os validadores `Integer`, `String` e `Float` do arquivo `validate.py`. Em seguida, testamos o validador `Integer` tentando verificar um valor inteiro (`42`) e um valor string (`"Hello"`). Se a verificação passar para o inteiro, imprimimos uma mensagem de sucesso. Se passar incorretamente para a string, imprimimos uma mensagem de erro. Se a verificação levantar corretamente um `TypeError` para a string, imprimimos uma mensagem de sucesso. Fazemos um teste semelhante para o validador `String`.

Depois de adicionar o código, execute o arquivo de teste usando o seguinte comando:

```bash
python3 /home/labex/project/test.py
```

Você deve ver uma saída semelhante a esta:

```
Testing Integer validator:
✓ Integer check passed for 42
✓ Correctly raised error: Expected <class 'int'>

Testing String validator:
✓ String check passed for 'Hello'
```

Como você pode ver, essas classes validadoras nos permitem realizar a verificação de tipo facilmente. Por exemplo, quando você chama `Integer.check(x)`, ele levantará um `TypeError` se `x` não for um inteiro.

Agora, vamos pensar em um cenário prático. Suponha que temos uma função que exige que seus argumentos sejam de tipos específicos. Aqui está um exemplo de tal função:

```python
def add(x, y):
    Integer.check(x)  # Make sure x is an integer
    Integer.check(y)  # Make sure y is an integer
    return x + y
```

Esta função funciona, mas há um problema. Temos que adicionar manualmente as verificações do validador toda vez que quisermos usar a verificação de tipo. Isso pode ser demorado e propenso a erros, especialmente para funções ou projetos maiores.

Nos próximos passos, resolveremos esse problema criando um objeto chamável. Este objeto será capaz de aplicar automaticamente essas verificações de tipo com base nas anotações de função. Dessa forma, não teremos que adicionar as verificações manualmente toda vez.
