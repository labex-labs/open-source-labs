# Usando `locals()` para Acessar Argumentos de Função

Em Python, entender os escopos de variáveis é crucial. O escopo de uma variável determina onde no código ela pode ser acessada. Python fornece uma função embutida chamada `locals()` que é muito útil para iniciantes entenderem o escopo. A função `locals()` retorna um dicionário contendo todas as variáveis locais no escopo atual. Isso pode ser extremamente útil quando você deseja inspecionar argumentos de função, pois fornece uma visão clara de quais variáveis estão disponíveis dentro de uma parte específica do seu código.

Vamos criar um experimento simples no interpretador Python para ver como isso funciona. Primeiro, precisamos navegar até o diretório do projeto e iniciar o interpretador Python. Você pode fazer isso executando os seguintes comandos no seu terminal:

```bash
cd ~/project
python3
```

Depois de entrar no shell interativo do Python, definiremos uma classe `Stock`. Uma classe em Python é como um modelo para criar objetos. Nesta classe, usaremos o método especial `__init__`. O método `__init__` é um construtor em Python, o que significa que ele é chamado automaticamente quando um objeto da classe é criado. Dentro deste método `__init__`, usaremos a função `locals()` para imprimir todas as variáveis locais.

```python
class Stock:
    def __init__(self, name, shares, price):
        print(locals())
```

Agora, vamos criar uma instância desta classe `Stock`. Uma instância é um objeto real criado a partir do modelo da classe. Passaremos alguns valores para os parâmetros `name`, `shares` e `price`.

```python
s = Stock('GOOG', 100, 490.1)
```

Quando você executar este código, deverá ver uma saída semelhante a:

```
{'self': <__main__.Stock object at 0x...>, 'name': 'GOOG', 'shares': 100, 'price': 490.1}
```

Esta saída mostra que `locals()` nos dá um dicionário contendo todas as variáveis locais no método `__init__`. A referência `self` é uma variável especial em classes Python que se refere à instância da própria classe. As outras variáveis são os valores dos parâmetros que passamos ao criar o objeto `Stock`.

Podemos usar essa funcionalidade `locals()` para inicializar automaticamente atributos de objeto. Atributos são variáveis associadas a um objeto. Vamos definir uma função auxiliar e modificar nossa classe `Stock`.

```python
def _init(locs):
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)

class Stock:
    def __init__(self, name, shares, price):
        _init(locals())
```

A função `_init` recebe o dicionário de variáveis locais obtido de `locals()`. Primeiro, ela remove a referência `self` do dicionário usando o método `pop`. Em seguida, ela itera sobre os pares chave-valor restantes no dicionário e usa a função `setattr` para definir cada variável como um atributo no objeto.

Agora, vamos testar esta implementação com argumentos posicionais e de palavra-chave. Argumentos posicionais são passados na ordem em que são definidos na assinatura da função, enquanto argumentos de palavra-chave são passados com os nomes dos parâmetros especificados.

```python
# Test with positional arguments
s1 = Stock('GOOG', 100, 490.1)
print(s1.name, s1.shares, s1.price)

# Test with keyword arguments
s2 = Stock(name='AAPL', shares=50, price=125.3)
print(s2.name, s2.shares, s2.price)
```

Ambas as abordagens devem funcionar agora! A função `_init` nos permite lidar com argumentos posicionais e de palavra-chave perfeitamente. Ela também preserva os nomes dos parâmetros na assinatura da função, o que torna a saída de `help()` mais útil. A função `help()` em Python fornece informações sobre funções, classes e módulos, e ter os nomes dos parâmetros intactos torna essa informação mais significativa.

Quando terminar de experimentar, você pode sair do interpretador Python executando o seguinte comando:

```python
exit()
```
