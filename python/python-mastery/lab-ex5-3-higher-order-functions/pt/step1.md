# Compreendendo a Duplicação de Código

Vamos começar analisando o código atual no arquivo `reader.py`. Em programação, examinar o código existente é um passo importante para entender como as coisas funcionam e identificar áreas para melhoria. Você pode abrir o arquivo `reader.py` no WebIDE. Existem duas maneiras de fazer isso. Você pode clicar no arquivo no explorador de arquivos ou pode executar os seguintes comandos no terminal. Esses comandos primeiro navegam até o diretório do projeto e, em seguida, exibem o conteúdo do arquivo `reader.py`.

```bash
cd ~/project
cat reader.py
```

Ao olhar para o código, você notará que existem duas funções. Funções em Python são blocos de código que executam uma tarefa específica. Aqui estão as duas funções e o que elas fazem:

1. `csv_as_dicts()`: Esta função recebe dados CSV e os converte em uma lista de dicionários. Um dicionário em Python é uma coleção de pares chave-valor, o que é útil para armazenar dados de forma estruturada.
2. `csv_as_instances()`: Esta função recebe dados CSV e os converte em uma lista de instâncias. Uma instância é um objeto criado a partir de uma classe, que é um modelo para criar objetos.

Agora, vamos dar uma olhada mais de perto nessas duas funções. Você verá que elas são bastante semelhantes. Ambas as funções seguem estas etapas:

- Primeiro, elas inicializam uma lista `records` vazia. Uma lista em Python é uma coleção de itens que podem ser de diferentes tipos. Inicializar uma lista vazia significa criar uma lista sem nenhum item, que será usada para armazenar os dados processados.
- Em seguida, elas usam `csv.reader()` para analisar a entrada. Analisar (parsing) significa analisar os dados de entrada para extrair informações significativas. Neste caso, `csv.reader()` nos ajuda a ler os dados CSV linha por linha.
- Elas lidam com os cabeçalhos da mesma forma. Os cabeçalhos em um arquivo CSV são a primeira linha que geralmente contém os nomes das colunas.
- Depois disso, elas percorrem cada linha nos dados CSV. Um loop é uma construção de programação que permite que você execute um bloco de código várias vezes.
- Para cada linha, elas a processam para criar um registro. Este registro pode ser um dicionário ou uma instância, dependendo da função.
- Elas anexam o registro à lista `records`. Anexar (appending) significa adicionar um item ao final da lista.
- Finalmente, elas retornam a lista `records`, que contém todos os dados processados.

Essa duplicação de código é um problema por vários motivos. Quando o código é duplicado:

- Torna-se mais difícil de manter. Se você precisar fazer uma alteração no código, você tem que fazer a mesma alteração em vários lugares. Isso leva mais tempo e esforço.
- Quaisquer alterações devem ser implementadas em vários lugares. Isso aumenta a chance de você esquecer de fazer a alteração em um dos lugares, levando a um comportamento inconsistente.
- Também aumenta a chance de introduzir bugs. Bugs são erros no código que podem fazer com que ele se comporte de forma inesperada.

A única diferença real entre essas duas funções é como elas convertem uma linha em um registro. Esta é uma situação clássica onde uma função de ordem superior pode ser muito útil. Uma função de ordem superior é uma função que pode receber outra função como argumento ou retornar uma função como resultado.

Vamos analisar alguns exemplos de uso dessas funções para entender melhor como elas funcionam. O código a seguir mostra como usar `csv_as_dicts()` e `csv_as_instances()`:

```python
# Example of using csv_as_dicts
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # {'name': 'AA', 'shares': 100, 'price': 32.2}

# Example of using csv_as_instances
class Stock:
    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

with open('portfolio.csv') as f:
    portfolio = csv_as_instances(f, Stock)
print(portfolio[0].name, portfolio[0].shares, portfolio[0].price)  # AA 100 32.2
```

Na próxima etapa, criaremos uma função de ordem superior para eliminar essa duplicação de código. Isso tornará o código mais fácil de manter e menos propenso a erros.
