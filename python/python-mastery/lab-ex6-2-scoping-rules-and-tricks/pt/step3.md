# Explorando a Inspeção do Frame da Pilha

A abordagem `_init(locals())` que temos usado é funcional, mas tem uma desvantagem. Toda vez que definimos um método `__init__`, temos que chamar explicitamente `locals()`. Isso pode se tornar um pouco complicado, especialmente ao lidar com várias classes. Felizmente, podemos tornar nosso código mais limpo e eficiente usando a inspeção do frame da pilha (stack frame inspection). Essa técnica nos permite acessar automaticamente as variáveis locais do chamador sem ter que chamar `locals()` explicitamente.

Vamos começar a explorar essa técnica no interpretador Python. Primeiro, abra seu terminal e navegue até o diretório do projeto. Em seguida, inicie o interpretador Python. Você pode fazer isso executando os seguintes comandos:

```bash
cd ~/project
python3
```

Agora que estamos no interpretador Python, precisamos importar o módulo `sys`. O módulo `sys` fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador Python. Usaremos isso para acessar as informações do frame da pilha.

```python
import sys
```

Em seguida, definiremos uma versão aprimorada de nossa função `_init()`. Esta nova versão acessará o frame do chamador diretamente, eliminando a necessidade de passar `locals()` explicitamente.

```python
def _init():
    # Get the caller's frame (1 level up in the call stack)
    frame = sys._getframe(1)

    # Get the local variables from that frame
    locs = frame.f_locals

    # Extract self and set other variables as attributes
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)
```

Neste código, `sys._getframe(1)` recupera o objeto frame da função chamadora. O `1` como argumento significa que estamos olhando um nível acima na pilha de chamadas (call stack). Depois de termos o objeto frame, podemos acessar suas variáveis locais usando `frame.f_locals`. Isso nos dá um dicionário de todas as variáveis locais no escopo do chamador. Em seguida, extraímos a variável `self` e definimos as variáveis restantes como atributos do objeto `self`.

Agora, vamos testar esta nova função `_init()` com uma nova versão de nossa classe `Stock`.

```python
class Stock:
    def __init__(self, name, shares, price):
        _init()  # No need to pass locals() anymore!

# Test it
s = Stock('GOOG', 100, 490.1)
print(s.name, s.shares, s.price)

# Also works with keyword arguments
s = Stock(name='AAPL', shares=50, price=125.3)
print(s.name, s.shares, s.price)
```

Como você pode ver, o método `__init__` não precisa mais passar `locals()` explicitamente. Isso torna nosso código mais limpo e fácil de ler da perspectiva do chamador.

### Como a Inspeção do Frame da Pilha Funciona

Quando você chama `sys._getframe(1)`, o Python retorna o objeto frame que representa o frame de execução do chamador. O argumento `1` significa "um nível acima do frame atual" (a função chamadora).

Um objeto frame contém informações importantes sobre o contexto de execução. Isso inclui a função atual sendo executada, as variáveis locais nessa função e o número da linha atualmente sendo executada.

Ao acessar `frame.f_locals`, obtemos um dicionário de todas as variáveis locais no escopo do chamador. Isso é semelhante ao que `locals()` retornaria se fosse chamado diretamente desse escopo.

Essa técnica é bastante poderosa, mas deve ser usada com cautela. É geralmente considerada um recurso avançado do Python e pode parecer um pouco "mágica" porque atinge fora dos limites normais de escopo do Python.

Depois de terminar de experimentar com a inspeção do frame da pilha, você pode sair do interpretador Python executando o seguinte comando:

```python
exit()
```
