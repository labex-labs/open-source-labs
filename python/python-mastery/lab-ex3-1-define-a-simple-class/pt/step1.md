# Adicionando um Método `sell` à Classe `Stock`

Nesta etapa, vamos aprimorar a classe `Stock` adicionando um novo método. Um método é como uma função especial que pertence a uma classe e pode trabalhar com os objetos criados a partir dessa classe. Criaremos um método chamado `sell(nshares)` que nos ajudará a simular a ação de vender ações de uma ação. Quando você vende ações, o número de ações que você possui diminui, e este método lidará com essa redução para nós.

## O que é um Método?

Vamos primeiro entender o que é um método. Um método é uma função que é definida dentro de uma classe. Ele é projetado para operar em instâncias (que são como cópias individuais) dessa classe. Quando um método é chamado em um objeto, ele pode acessar todos os atributos (características) desse objeto. Ele faz isso através do parâmetro `self`. O parâmetro `self` é uma referência ao objeto no qual o método está sendo chamado. Portanto, quando você usa `self` dentro de um método, você está se referindo ao objeto específico em que o método está atuando.

## Instruções de Implementação

1. Primeiro, precisamos abrir o arquivo `stock.py` no editor. Para fazer isso, usaremos a linha de comando. Abra seu terminal e execute o seguinte comando. Este comando altera o diretório para a pasta `project` onde o arquivo `stock.py` está localizado.

```bash
cd ~/project
```

2. Depois de abrir o arquivo `stock.py`, você precisa encontrar um comentário específico na classe `Stock`. Procure o comentário `# TODO: Add sell(nshares) method here`. Este comentário é um espaço reservado que indica onde devemos adicionar nosso novo método `sell`.

3. Agora, é hora de adicionar o método `sell`. Este método receberá um parâmetro chamado `nshares`, que representa o número de ações que você deseja vender. O trabalho principal deste método é diminuir o atributo `shares` do objeto `Stock` pelo número de ações que você está vendendo.

Aqui está o código para o método `sell` que você precisa adicionar:

```python
def sell(self, nshares):
    self.shares -= nshares
```

Neste código, `self.shares` se refere ao atributo `shares` do objeto `Stock`. O operador `-=` subtrai o valor de `nshares` do valor atual de `self.shares`.

4. Depois de adicionar o método `sell`, você precisa salvar o arquivo `stock.py`. Você pode fazer isso pressionando `Ctrl+S` no seu teclado ou selecionando "File > Save" no menu do seu editor.

5. Para garantir que nosso método `sell` funcione corretamente, criaremos um script de teste. Crie um novo arquivo Python chamado `test_sell.py` e adicione o seguinte código a ele:

```python
# test_sell.py
from stock import Stock

# Create a stock object
s = Stock('GOOG', 100, 490.10)
print(f"Initial shares: {s.shares}")

# Sell 25 shares
s.sell(25)
print(f"Shares after selling: {s.shares}")
```

Neste script, primeiro importamos a classe `Stock` do arquivo `stock.py`. Em seguida, criamos um objeto `Stock` chamado `s` com o símbolo da ação `GOOG`, 100 ações e um preço de 490.10. Imprimimos o número inicial de ações. Depois disso, chamamos o método `sell` no objeto `s` para vender 25 ações. Finalmente, imprimimos o número de ações após a venda.

6. Agora, executaremos o script de teste para ver se nosso método `sell` está funcionando como esperado. Abra seu terminal novamente e execute o seguinte comando:

```bash
python3 test_sell.py
```

Se tudo estiver funcionando corretamente, você deverá ver uma saída semelhante a esta:

```
Initial shares: 100
Shares after selling: 75
```

Esta saída confirma que nosso método `sell` está funcionando corretamente. Ele reduziu com sucesso o número de ações pela quantidade que especificamos.
