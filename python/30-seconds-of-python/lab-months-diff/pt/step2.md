# Criando a Função de Diferença de Meses

Agora que entendemos como trabalhar com objetos de data e calcular a diferença em dias, vamos criar uma função para calcular a diferença em meses.

Em muitas aplicações, um mês é aproximado como 30 dias. Embora isso nem sempre seja preciso (os meses podem ter de 28 a 31 dias), é uma simplificação comum que funciona bem para muitos cálculos comerciais.

Abra seu arquivo `month_difference.py` e adicione esta função abaixo do seu código existente:

```python
def months_diff(start, end):
    """
    Calculate the difference in months between two dates.

    Args:
        start (date): The start date
        end (date): The end date

    Returns:
        int: The number of months between the dates (rounded up)
    """
    # Calculate the difference in days
    days_difference = (end - start).days

    # Convert days to months (assuming 30 days per month) and round up
    months = ceil(days_difference / 30)

    return months
```

Vamos entender o que esta função faz:

1.  Ela recebe dois parâmetros: `start` e `end`, que são objetos de data
2.  Ela calcula a diferença em dias entre essas datas
3.  Ela divide por 30 para converter dias em meses
4.  Ela usa `ceil()` para arredondar para o inteiro mais próximo
5.  Ela retorna o resultado como um inteiro

A função `ceil()` é usada porque em muitos cenários de negócios, mesmo um mês parcial é contado como um mês inteiro para fins de faturamento.

Para testar nossa função, adicione o seguinte código no final do seu arquivo:

```python
# Test the months_diff function with our example dates
print(f"Months between {date1} and {date2}: {months_diff(date1, date2)}")

# Test with some other date pairs
print(f"Months between 2020-10-28 and 2020-11-25: {months_diff(date(2020, 10, 28), date(2020, 11, 25))}")
print(f"Months between 2020-12-15 and 2021-01-10: {months_diff(date(2020, 12, 15), date(2021, 01, 10))}")
```

Salve seu arquivo e execute-o novamente:

```bash
python3 ~/project/month_difference.py
```

Você deve ver uma saída como:

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
Months between 2023-01-15 and 2023-03-20: 3
Months between 2020-10-28 and 2020-11-25: 1
Months between 2020-12-15 and 2021-01-10: 1
```

Observe que:

- Os 64 dias entre 2023-01-15 e 2023-03-20 são calculados como 3 meses (64/30 = 2.13, arredondado para cima para 3)
- A diferença entre 28 de outubro e 25 de novembro é calculada como 1 mês
- A diferença entre 15 de dezembro e 10 de janeiro (atravessando uma fronteira de ano) também é calculada como 1 mês
