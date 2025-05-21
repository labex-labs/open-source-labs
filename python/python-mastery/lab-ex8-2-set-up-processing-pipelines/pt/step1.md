# Pipeline de Gerador Básico com Dados CSV

Nesta etapa, vamos aprender como criar um pipeline de processamento básico usando geradores. Mas primeiro, vamos entender o que são geradores. Geradores são um tipo especial de iterador em Python. Ao contrário dos iteradores regulares que podem carregar todos os dados na memória de uma vez, os geradores geram valores sob demanda. Isso é extremamente útil ao lidar com grandes fluxos de dados, pois economiza memória. Em vez de ter que armazenar todo o conjunto de dados na memória, o gerador produz valores um por um conforme você precisa deles.

## Entendendo Geradores

Um gerador é essencialmente uma função que retorna um iterador. Quando você itera sobre este iterador, ele produz uma sequência de valores. A maneira como você escreve uma função geradora é semelhante a uma função regular, mas há uma diferença fundamental. Em vez de usar a instrução `return`, uma função geradora usa a instrução `yield`. A instrução `yield` tem um comportamento único. Ela pausa a função e salva seu estado atual. Quando o próximo valor é solicitado, a função continua de onde parou. Isso permite que o gerador produza valores incrementalmente sem ter que começar do início toda vez.

## Usando a Função follow()

A função `follow()` que você criou anteriormente funciona de maneira semelhante ao comando Unix `tail -f`. O comando `tail -f` monitora continuamente um arquivo em busca de novo conteúdo, e a função `follow()` faz o mesmo. Agora, vamos usá-la para criar um pipeline de processamento simples.

### Passo 1: Abra uma nova janela de terminal

Primeiro, abra uma nova janela de terminal no WebIDE. Você pode fazer isso indo em `Terminal → New Terminal`. Este novo terminal será onde executaremos nossos comandos Python.

### Passo 2: Inicie um shell interativo Python

Depois que o novo terminal estiver aberto, inicie um shell interativo Python. Você pode fazer isso digitando o seguinte comando no terminal:

```bash
python3
```

O shell interativo Python permite que você execute o código Python linha por linha e veja os resultados imediatamente.

### Passo 3: Importe a função `follow` e configure o pipeline

Agora, importaremos a função `follow` e configuraremos um pipeline básico para ler os dados das ações. No shell interativo Python, digite o seguinte código:

```python
>>> from follow import follow
>>> import csv
>>> lines = follow('stocklog.csv')
>>> rows = csv.reader(lines)
>>> for row in rows:
...     print(row)
...
```

Aqui está o que cada linha faz:

- `from follow import follow`: Isso importa a função `follow` do módulo `follow`.
- `import csv`: Isso importa o módulo `csv`, que é usado para ler e escrever arquivos CSV em Python.
- `lines = follow('stocklog.csv')`: Isso chama a função `follow` com o nome do arquivo `stocklog.csv`. A função `follow` retorna um gerador que produz novas linhas à medida que são adicionadas ao arquivo.
- `rows = csv.reader(lines)`: A função `csv.reader()` pega as linhas geradas pela função `follow` e as analisa em linhas de dados CSV.
- O loop `for` itera por essas linhas e imprime cada uma.

### Passo 4: Verifique a saída

Após executar o código, você deve ver uma saída semelhante a esta (seus dados variarão):

```
['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
...
```

Esta saída indica que você criou um pipeline de dados com sucesso. A função `follow()` gera linhas do arquivo, e essas linhas são então passadas para a função `csv.reader()`, que as analisa em linhas de dados.

Se você viu saída suficiente, pode parar a execução pressionando `Ctrl+C`.

## O que está Acontecendo?

Vamos detalhar o que está acontecendo neste pipeline:

1. `follow('stocklog.csv')` cria um gerador. Este gerador acompanha o arquivo `stocklog.csv` e produz novas linhas à medida que são adicionadas ao arquivo.
2. `csv.reader(lines)` pega as linhas geradas pela função `follow` e as analisa em dados de linha CSV. Ele entende a estrutura dos arquivos CSV e divide as linhas em valores individuais.
3. O loop `for` então itera por essas linhas, imprimindo cada uma. Isso permite que você veja os dados em um formato legível.

Este é um exemplo simples de um pipeline de processamento de dados usando geradores. Nas próximas etapas, construiremos pipelines mais complexos e úteis.
