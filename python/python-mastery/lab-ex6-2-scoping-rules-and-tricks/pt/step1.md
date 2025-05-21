# Compreendendo o Problema com a Inicialização de Classes

No mundo da programação, as classes são um conceito fundamental que permite criar tipos de dados personalizados. Em exercícios anteriores, você pode ter criado uma classe `Structure`. Essa classe serve como uma ferramenta útil para definir facilmente estruturas de dados. Uma estrutura de dados é uma maneira de organizar e armazenar dados para que possam ser acessados e usados eficientemente. A classe `Structure`, como uma classe base, cuida da inicialização de atributos com base em uma lista predefinida de nomes de campos. Atributos são variáveis que pertencem a um objeto, e nomes de campos são os nomes que damos a esses atributos.

Vamos dar uma olhada mais de perto na implementação atual da classe `Structure`. Para fazer isso, precisamos abrir o arquivo `structure.py` no editor de código. Este arquivo contém o código para a classe `Structure`. Aqui estão os comandos para navegar até o diretório do projeto e abrir o arquivo:

```bash
cd ~/project
code structure.py
```

A classe `Structure` fornece uma estrutura básica para definir estruturas de dados simples. Quando criamos uma subclasse, como a classe `Stock`, podemos definir os campos específicos que queremos para essa subclasse. Uma subclasse herda as propriedades e métodos de sua classe base, neste caso, a classe `Structure`. Por exemplo, na classe `Stock`, definimos os campos `name`, `shares` e `price`:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')
```

Agora, vamos abrir o arquivo `stock.py` para ver como a classe `Stock` é implementada no contexto do código geral. Este arquivo provavelmente contém o código que usa a classe `Stock` e interage com ela. Use o seguinte comando para abrir o arquivo:

```bash
code stock.py
```

Embora essa abordagem de usar a classe `Structure` e suas subclasses funcione, ela tem várias limitações. Para identificar esses problemas, executaremos o interpretador Python e exploraremos como a classe `Stock` se comporta. O seguinte comando importará a classe `Stock` e exibirá suas informações de ajuda:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Ao executar este comando, você notará que a assinatura mostrada na saída de ajuda não é muito útil. Em vez de mostrar os nomes reais dos parâmetros, como `name`, `shares` e `price`, ela mostra apenas `*args`. Essa falta de nomes de parâmetros claros dificulta para os usuários entender como criar corretamente uma instância da classe `Stock`.

Vamos também tentar criar uma instância `Stock` usando argumentos de palavra-chave (keyword arguments). Argumentos de palavra-chave permitem que você especifique os valores dos parâmetros por seus nomes, o que pode tornar o código mais legível. Execute o seguinte comando:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

Você deve obter uma mensagem de erro como esta:

```
TypeError: __init__() got an unexpected keyword argument 'name'
```

Este erro ocorre porque nosso método `__init__` atual, que é responsável por inicializar objetos da classe `Stock`, não lida com argumentos de palavra-chave. Ele aceita apenas argumentos posicionais, o que significa que você deve fornecer os valores em uma ordem específica sem usar os nomes dos parâmetros. Esta é uma limitação que queremos corrigir neste laboratório.

Neste laboratório, exploraremos diferentes abordagens para tornar nossa classe `Structure` mais flexível e amigável para o usuário. Ao fazer isso, podemos melhorar a usabilidade da classe `Stock` e outras subclasses de `Structure`.
