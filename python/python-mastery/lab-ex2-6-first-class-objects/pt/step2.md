# Criando uma Função Utilitária para Processamento CSV

Agora que entendemos como os objetos de primeira classe (first-class objects) do Python podem nos ajudar com a conversão de dados, vamos criar uma função utilitária reutilizável. Esta função lerá dados CSV e os transformará em uma lista de dicionários. Esta é uma operação muito útil porque os arquivos CSV são comumente usados para armazenar dados tabulares, e convertê-los em uma lista de dicionários facilita o trabalho com os dados em Python.

## Criando o Utilitário de Leitura CSV

Primeiro, abra o WebIDE. Depois de aberto, navegue até o diretório do projeto e crie um novo arquivo chamado `reader.py`. Neste arquivo, definiremos uma função que lê dados CSV e aplica conversões de tipo. As conversões de tipo são importantes porque os dados em um arquivo CSV geralmente são lidos como strings, mas podemos precisar de diferentes tipos de dados, como inteiros ou números de ponto flutuante, para processamento posterior.

Adicione o seguinte código a `reader.py`:

```python
import csv

def read_csv_as_dicts(filename, types):
    """
    Leia um arquivo CSV em uma lista de dicionários, convertendo cada campo de acordo
    com os tipos fornecidos.

    Parâmetros:
    filename (str): Nome do arquivo CSV a ser lido
    types (list): Lista de funções de conversão de tipo para cada coluna

    Retorna:
    list: Lista de dicionários representando os dados CSV
    """
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Obtenha os cabeçalhos das colunas

        for row in rows:
            # Aplique conversões de tipo a cada valor na linha
            converted_row = [func(val) for func, val in zip(types, row)]

            # Crie um dicionário mapeando os cabeçalhos para os valores convertidos
            record = dict(zip(headers, converted_row))
            records.append(record)

    return records
```

Esta função primeiro abre o arquivo CSV especificado. Em seguida, lê os cabeçalhos do arquivo CSV, que são os nomes das colunas. Depois disso, ela percorre cada linha no arquivo. Para cada valor na linha, ela aplica a função de conversão de tipo correspondente da lista `types`. Finalmente, ela cria um dicionário onde as chaves são os cabeçalhos das colunas e os valores são os dados convertidos, e adiciona este dicionário à lista `records`. Depois que todas as linhas são processadas, ela retorna a lista `records`.

## Testando a Função Utilitária

Vamos testar nossa função utilitária. Primeiro, abra um terminal e inicie um interpretador Python digitando:

```bash
python3
```

Agora que estamos no interpretador Python, podemos usar nossa função para ler os dados do portfólio. Os dados do portfólio são um arquivo CSV que contém informações sobre ações, como o nome da ação, o número de ações e o preço.

```python
import reader
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
for record in portfolio[:3]:  # Mostre os primeiros 3 registros
    print(record)
```

Quando você executar este código, deverá ver uma saída semelhante a:

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
{'name': 'CAT', 'shares': 150, 'price': 83.44}
```

Esta saída mostra os três primeiros registros dos dados do portfólio, com os tipos de dados corretamente convertidos.

Vamos também testar nossa função com os dados do ônibus CTA. Os dados do ônibus CTA são outro arquivo CSV que contém informações sobre rotas de ônibus, datas, tipos de dia e o número de viagens.

```python
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])
print(f"Total rows: {len(rows)}")
print("First row:", rows[0])
```

A saída deve ser algo como:

```
Total rows: 577563
First row: {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

Isso mostra que nossa função pode lidar com diferentes arquivos CSV e aplicar as conversões de tipo apropriadas.

Para sair do interpretador Python, digite:

```python
exit()
```

Você agora criou uma função utilitária reutilizável que pode ler qualquer arquivo CSV e aplicar as conversões de tipo apropriadas. Isso demonstra o poder dos objetos de primeira classe do Python e como eles podem ser usados para criar um código flexível e reutilizável.
