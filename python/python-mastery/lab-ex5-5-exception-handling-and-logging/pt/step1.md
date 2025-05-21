# Compreendendo Exceções em Python

Nesta etapa, vamos aprender sobre exceções em Python. Exceções são um conceito importante em programação. Elas nos ajudam a lidar com situações inesperadas que podem ocorrer enquanto um programa está sendo executado. Também vamos descobrir por que o código atual trava quando tenta processar dados inválidos. Compreender isso o ajudará a escrever programas Python mais robustos e confiáveis.

## O que são Exceções?

Em Python, exceções são eventos que acontecem durante a execução de um programa e interrompem o fluxo normal de instruções. Pense nisso como um bloqueio em uma rodovia. Quando tudo corre bem, seu programa segue um caminho definido, assim como um carro em uma estrada livre. Mas quando um erro ocorre, o Python cria um objeto de exceção. Esse objeto é como um relatório que contém informações sobre o que deu errado, como o tipo de erro e onde ele aconteceu no código.

Se essas exceções não forem tratadas adequadamente, elas farão com que o programa trave. Quando uma falha ocorre, o Python mostra uma mensagem de traceback (rastreamento). Essa mensagem é como um mapa que mostra a localização exata no código onde o erro ocorreu. É muito útil para depuração.

## Examinando o Código Atual

Vamos primeiro dar uma olhada na estrutura do arquivo `reader.py`. Este arquivo contém funções que são usadas para ler e converter dados CSV. Para abrir o arquivo no editor, precisamos navegar para o diretório correto. Usaremos o comando `cd` no terminal.

```bash
cd /home/labex/project
```

Agora que estamos no diretório certo, vamos ver o conteúdo de `reader.py`. Este arquivo tem várias funções importantes:

1. `convert_csv()`: Esta função recebe linhas de dados e usa uma função conversora fornecida para convertê-las. É como uma máquina que pega matérias-primas (linhas de dados) e as transforma em uma forma diferente de acordo com uma receita específica (a função conversora).
2. `csv_as_dicts()`: Esta função lê dados CSV e os transforma em uma lista de dicionários. Ela também realiza a conversão de tipos, o que significa que garante que cada dado no dicionário seja do tipo correto, como uma string, um inteiro ou um float.
3. `read_csv_as_dicts()`: Esta é uma função wrapper (envoltório). É como um gerente que chama a função `csv_as_dicts()` para fazer o trabalho.

## Demonstrando o Problema

Vamos ver o que acontece quando o código tenta processar dados inválidos. Vamos abrir um interpretador Python, que é como um playground onde podemos testar nosso código Python interativamente. Para abrir o interpretador Python, usaremos o seguinte comando no terminal:

```bash
python3
```

Depois que o interpretador Python estiver aberto, tentaremos ler o arquivo `missing.csv`. Este arquivo contém alguns dados ausentes ou inválidos. Usaremos a função `read_csv_as_dicts()` do arquivo `reader.py` para ler os dados.

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
```

Quando você executar este código, deverá ver uma mensagem de erro como esta:

```
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: ''
```

Este erro ocorre porque o código tenta converter uma string vazia em um inteiro. Uma string vazia não representa um inteiro válido, então o Python não pode fazer a conversão. A função trava no primeiro erro que encontra e para de processar o restante dos dados válidos no arquivo.

Para sair do interpretador Python, digite o seguinte comando:

```python
exit()
```

## Compreendendo o Fluxo de Erro

O erro acontece na função `convert_csv()`, especificamente na seguinte linha:

```python
return list(map(lambda row: converter(headers, row), rows))
```

A função `map()` aplica a função `converter` a cada linha na lista `rows`. A função `converter` tenta aplicar os tipos (str, int, float) a cada linha. Mas quando encontra uma linha com dados ausentes, ela falha. A função `map()` não tem uma maneira integrada de lidar com exceções. Então, quando uma exceção ocorre, todo o processo trava.

Na próxima etapa, você modificará o código para lidar com essas exceções de forma elegante. Isso significa que, em vez de travar, o programa será capaz de lidar com os erros e continuar processando o restante dos dados.
