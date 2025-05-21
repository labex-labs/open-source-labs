# Implementando o Tratamento de Exceções

Nesta etapa, vamos nos concentrar em tornar seu código mais robusto. Quando um programa encontra dados ruins, ele geralmente trava. Mas podemos usar uma técnica chamada tratamento de exceções para lidar com esses problemas de forma elegante. Você modificará o arquivo `reader.py` para implementar isso. O tratamento de exceções permite que seu programa continue sendo executado mesmo quando enfrenta dados inesperados, em vez de parar abruptamente.

## Compreendendo os Blocos Try-Except

Python oferece uma maneira poderosa de lidar com exceções usando blocos try-except. Vamos detalhar como eles funcionam.

```python
try:
    # Código que pode causar uma exceção
    result = risky_operation()
except SomeExceptionType as e:
    # Código que é executado se a exceção ocorrer
    handle_exception(e)
```

No bloco `try`, você coloca o código que pode gerar uma exceção. Uma exceção é um erro que ocorre durante a execução de um programa. Por exemplo, se você tentar dividir um número por zero, o Python gerará uma exceção `ZeroDivisionError`. Quando uma exceção ocorre no bloco `try`, o Python para de executar o código no bloco `try` e pula para o bloco `except` correspondente. O bloco `except` contém o código que tratará a exceção. O `SomeExceptionType` é o tipo de exceção que você deseja capturar. Você pode capturar tipos específicos de exceções ou usar um `Exception` geral para capturar todos os tipos de exceções. A parte `as e` permite que você acesse o objeto de exceção, que contém informações sobre o erro.

## Modificando o Código

Agora, vamos aplicar o que aprendemos sobre blocos try-except à função `convert_csv()`. Abra o arquivo `reader.py` em seu editor.

1. Substitua a função `convert_csv()` atual pelo seguinte código:

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Print a warning message for bad rows
            print(f"Row {row_idx}: Bad row: {row}")
            continue

    return result
```

Nesta nova implementação:

- Usamos um loop `for` em vez de `map()` para processar cada linha. Isso nos dá mais controle sobre o processamento de cada linha.
- Envolvemos o código de conversão em um bloco try-except. Isso significa que, se uma exceção ocorrer durante a conversão de uma linha, o programa não travará. Em vez disso, ele pulará para o bloco `except`.
- No bloco `except`, imprimimos uma mensagem de erro para linhas inválidas. Isso nos ajuda a identificar quais linhas têm problemas.
- Depois de imprimir a mensagem de erro, usamos a instrução `continue` para pular a linha atual e continuar processando as linhas restantes.

Salve o arquivo após fazer essas alterações.

## Testando suas Mudanças

Vamos testar seu código modificado com o arquivo `missing.csv`. Primeiro, abra o interpretador Python executando o seguinte comando em seu terminal:

```bash
python3
```

Depois de estar no interpretador Python, execute o seguinte código:

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

Quando você executar este código, deverá ver mensagens de erro para cada linha problemática. Mas o programa continuará processando e retornará as linhas válidas. Aqui está um exemplo do que você pode ver:

```
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
Number of valid rows processed: 20
```

Vamos também verificar se o programa funciona corretamente com dados válidos. Execute o seguinte código no interpretador Python:

```python
valid_port = read_csv_as_dicts('valid.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(valid_port)}")
```

Você deve ver que todas as linhas são processadas sem erros. Aqui está um exemplo da saída:

```
Number of valid rows processed: 17
```

Para sair do interpretador Python, execute o seguinte comando:

```python
exit()
```

Agora seu código é mais robusto. Ele pode lidar com dados inválidos de forma elegante, ignorando linhas ruins em vez de travar. Isso torna seu programa mais confiável e fácil de usar.
