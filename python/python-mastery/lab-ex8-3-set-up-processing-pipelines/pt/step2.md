# Criando Componentes de Pipeline de Corrotina

Nesta etapa, vamos criar corrotinas mais especializadas para processar dados de ações. Uma corrotina é um tipo especial de função que pode pausar e retomar sua execução, o que é muito útil para construir pipelines de processamento de dados. Cada corrotina que criamos executará uma tarefa específica em nosso pipeline geral de processamento.

1. Primeiro, você precisa criar um novo arquivo. Navegue até o diretório `/home/labex/project` e crie um arquivo chamado `coticker.py`. Este arquivo conterá todo o código para nosso processamento de dados baseado em corrotinas.

2. Agora, vamos começar a escrever código no arquivo `coticker.py`. Primeiro, importaremos os módulos necessários e definiremos a estrutura básica. Módulos são bibliotecas de código pré-escritas que fornecem funções e classes úteis. O seguinte código faz exatamente isso:

```python
# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

3. Ao olhar o código acima, você notará que há erros relacionados a `String()`, `Float()` e `Integer()`. Estas são classes que precisamos importar. Portanto, adicionaremos as importações necessárias no topo do arquivo. Desta forma, o Python sabe onde encontrar essas classes. Aqui está o código atualizado:

```python
# coticker.py
from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

4. Em seguida, adicionaremos os componentes de corrotina que formarão nosso pipeline de processamento de dados. Cada corrotina tem um trabalho específico no pipeline. Aqui está o código para adicionar essas corrotinas:

```python
@consumer
def to_csv(target):
    def producer():
        while True:
            line = yield

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
```

5. Vamos entender o que cada uma dessas corrotinas faz:
   - `to_csv`: Seu trabalho é converter linhas de texto bruto em linhas CSV analisadas. Isso é importante porque nossos dados estão inicialmente em formato de texto e precisamos dividi-los em dados CSV estruturados.
   - `create_ticker`: Esta corrotina pega as linhas CSV e cria objetos `Ticker` a partir delas. Os objetos `Ticker` representam os dados de ações de uma forma mais organizada.
   - `negchange`: Ele filtra os objetos `Ticker`. Ele só passa as ações que têm mudanças de preço negativas. Isso nos ajuda a nos concentrar nas ações que estão perdendo valor.
   - `ticker`: Esta corrotina formata e exibe os dados do ticker. Ele usa um formatador para apresentar os dados em uma tabela agradável e legível.

6. Finalmente, precisamos adicionar o código do programa principal que conecta todos esses componentes. Este código configurará o fluxo de dados através do pipeline. Aqui está o código:

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change']

    # Create the processing pipeline
    t = ticker('text', fields)
    neg_filter = negchange(t)
    tick_creator = create_ticker(neg_filter)
    csv_parser = to_csv(tick_creator)

    # Connect the pipeline to the data source
    follow('stocklog.csv', csv_parser)
```

7. Depois de escrever todo o código, salve o arquivo `coticker.py`. Em seguida, abra o terminal e execute os seguintes comandos. O comando `cd` altera o diretório para onde nosso arquivo está localizado, e o comando `python3` executa nosso script Python:

```bash
cd /home/labex/project
python3 coticker.py
```

8. Se tudo correr bem, você deverá ver uma tabela formatada no terminal. Esta tabela mostra ações com mudanças de preço negativas. A saída será algo parecido com isto:

```
      name      price     change
---------- ---------- ----------
      MSFT      72.50      -0.25
        AA      35.25      -0.15
       IBM      50.10      -0.15
      GOOG     100.02      -0.01
      AAPL     102.50      -0.06
```

Tenha em mente que os valores reais na tabela podem variar dependendo dos dados de ações gerados.

## Entendendo o Fluxo do Pipeline

A parte mais importante deste programa é como os dados fluem através das corrotinas. Vamos dividi-lo passo a passo:

1. A função `follow` começa lendo linhas do arquivo `stocklog.csv`. Esta é nossa fonte de dados.
2. Cada linha que é lida é então enviada para a corrotina `csv_parser`. O `csv_parser` pega a linha de texto bruto e a analisa em campos CSV.
3. Os dados CSV analisados são então enviados para a corrotina `tick_creator`. Esta corrotina cria objetos `Ticker` a partir das linhas CSV.
4. Os objetos `Ticker` são então enviados para a corrotina `neg_filter`. Esta corrotina verifica cada objeto `Ticker`. Se a ação tiver uma mudança de preço negativa, ela passa o objeto; caso contrário, ela o descarta.
5. Finalmente, os objetos `Ticker` filtrados são enviados para a corrotina `ticker`. A corrotina `ticker` formata os dados e os exibe em uma tabela.

Esta arquitetura de pipeline é muito útil porque permite que cada componente se concentre em uma única tarefa. Isso torna o código mais modular, o que significa que é mais fácil de entender, modificar e manter.
