# Adicionando Tratamento de Erros

Ao trabalhar com dados do mundo real, é muito comum encontrar inconsistências ou erros. Por exemplo, os dados podem ter valores ausentes, formatos incorretos ou outros problemas. Python oferece mecanismos de tratamento de exceções para lidar com essas situações de forma elegante. O tratamento de exceções permite que seu programa continue sendo executado mesmo quando encontra um erro, em vez de travar abruptamente.

## Entendendo o Problema

Vamos dar uma olhada no arquivo `portfolio3.dat`. Este arquivo contém alguns dados sobre um portfólio, como o símbolo da ação, o número de ações e o preço por ação. Para visualizar o conteúdo deste arquivo, podemos usar o seguinte comando:

```bash
cat /home/labex/project/portfolio3.dat
```

Ao executar este comando, você notará que algumas linhas no arquivo têm traços (`-`) em vez de números para as ações. Aqui está um exemplo do que você pode ver:

```
AA 100 32.20
IBM 50 91.10
C - 53.08
...
```

Se tentarmos executar nosso código atual neste arquivo, ele travará. A razão é que nosso código espera converter o número de ações em um inteiro, mas não pode converter um traço (`-`) em um inteiro. Vamos tentar executar o código e ver o que acontece:

```bash
python3 -c "import sys; sys.path.append('/home/labex/project'); from pcost import portfolio_cost; print(portfolio_cost('/home/labex/project/portfolio3.dat'))"
```

Você verá uma mensagem de erro como esta:

```
ValueError: invalid literal for int() with base 10: '-'
```

Este erro ocorre porque o Python não pode converter o caractere `-` em um inteiro quando tenta executar `int(fields[1])`.

## Introdução ao Tratamento de Exceções

O tratamento de exceções do Python usa blocos `try` e `except`. O bloco `try` contém o código que pode gerar uma exceção. Uma exceção é um erro que ocorre durante a execução de um programa. O bloco `except` contém o código que será executado se uma exceção ocorrer no bloco `try`.

Aqui está um exemplo de como os blocos `try` e `except` funcionam:

```python
try:
    # Código que pode gerar uma exceção
    result = risky_operation()
except ExceptionType as e:
    # Código para lidar com a exceção
    print(f"Ocorreu um erro: {e}")
```

Quando o Python executa o código no bloco `try`, se uma exceção ocorrer, a execução salta imediatamente para o bloco `except` correspondente. O `ExceptionType` no bloco `except` especifica o tipo de exceção que queremos tratar. A variável `e` contém informações sobre a exceção, como a mensagem de erro.

## Modificando a Função com Tratamento de Exceções

Vamos atualizar nosso arquivo `pcost.py` para lidar com erros nos dados. Usaremos os blocos `try` e `except` para pular as linhas com dados ruins e mostrar uma mensagem de aviso.

```python
def portfolio_cost(filename):
    """
    Computa o custo total (ações*preço) de um arquivo de portfólio
    Lida com linhas com dados ruins, ignorando-as e mostrando um aviso.

    Args:
        filename: O nome do arquivo de portfólio

    Returns:
        O custo total do portfólio como um float
    """
    total_cost = 0.0

    # Abre o arquivo e lê cada linha
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                # Extrai os dados (símbolo, ações, preço)
                shares = int(fields[1])
                price = float(fields[2])
                # Adiciona o custo ao nosso total acumulado
                total_cost += shares * price
            except ValueError as e:
                # Imprime um aviso para linhas que não podem ser analisadas
                print(f"Não foi possível analisar: '{line}'")
                print(f"Motivo: {e}")

    return total_cost

# Chama a função com o arquivo portfolio3.dat
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio3.dat')
    print(cost)
```

Neste código atualizado, primeiro abrimos o arquivo e o lemos linha por linha. Para cada linha, dividimos em campos. Em seguida, tentamos converter o número de ações em um inteiro e o preço em um float. Se essa conversão falhar (ou seja, ocorrer um `ValueError`), imprimimos uma mensagem de aviso e ignoramos essa linha. Caso contrário, calculamos o custo das ações e o adicionamos ao custo total.

## Testando a Função Atualizada

Agora, vamos executar o programa atualizado com o arquivo problemático. Primeiro, precisamos navegar até o diretório do projeto e, em seguida, podemos executar o script Python.

```bash
cd /home/labex/project
python3 pcost.py
```

Você deve ver uma saída como esta:

```
Não foi possível analisar: 'C - 53.08
'
Motivo: invalid literal for int() with base 10: '-'
Não foi possível analisar: 'DIS - 34.20
'
Motivo: invalid literal for int() with base 10: '-'
44671.15
```

O programa agora faz o seguinte:

1.  Ele tenta processar cada linha do arquivo.
2.  Se uma linha contiver dados inválidos, ele captura o `ValueError`.
3.  Ele imprime uma mensagem útil sobre o problema.
4.  Ele continua processando o restante do arquivo.
5.  Ele retorna o custo total com base nas linhas válidas.

Essa abordagem torna nosso programa muito mais robusto ao lidar com dados imperfeitos. Ele pode lidar com erros de forma elegante e ainda fornecer resultados úteis.
