# Criando uma Aplicação Prática: Calculadora de Assinatura

Agora que temos uma função confiável para calcular diferenças de meses, vamos aplicá-la a um cenário do mundo real. Criaremos uma calculadora de assinatura que determina o custo de uma assinatura de serviço entre duas datas.

Crie um novo arquivo chamado `subscription_calculator.py` no diretório `/home/labex/project`:

```python
from datetime import date, timedelta
from month_difference import months_diff

def calculate_subscription_cost(start_date, end_date, monthly_fee):
    """
    Calculate the total cost of a subscription between two dates.

    Args:
        start_date (date): Subscription start date
        end_date (date): Subscription end date
        monthly_fee (float): Cost per month

    Returns:
        float: Total subscription cost
    """
    # Calculate number of months
    months = months_diff(start_date, end_date)

    # Calculate total cost
    total_cost = months * monthly_fee

    return total_cost

# Example: Calculate subscription cost for a streaming service
start = date(2023, 1, 15)  # Subscription starts January 15, 2023
end = date(2023, 8, 20)    # Ends August 20, 2023
monthly_cost = 9.99        # $9.99 per month

total = calculate_subscription_cost(start, end, monthly_cost)
print(f"Subscription period: {start} to {end}")
print(f"Monthly fee: ${monthly_cost:.2f}")
print(f"Total cost: ${total:.2f}")

# Compare with an annual plan
annual_cost = 99.99  # $99.99 per year
print(f"\nAnnual plan cost: ${annual_cost:.2f}")
print(f"Monthly plan for same period: ${total:.2f}")

if total > annual_cost:
    print(f"Savings with annual plan: ${total - annual_cost:.2f}")
else:
    print(f"Additional cost for annual plan: ${annual_cost - total:.2f}")

# Calculate cost for a trial period
today = date.today()
trial_end = today + timedelta(days=7)  # 7-day trial
trial_cost = calculate_subscription_cost(today, trial_end, monthly_cost)
print(f"\nOne-week trial period: {today} to {trial_end}")
print(f"Trial period cost: ${trial_cost:.2f}")
```

Salve o arquivo e execute-o:

```bash
python3 ~/project/subscription_calculator.py
```

Você deve ver uma saída semelhante a esta (as datas de teste mostrarão sua data atual):

```
Subscription period: 2023-01-15 to 2023-08-20
Monthly fee: $9.99
Total cost: $79.92

Annual plan cost: $99.99
Monthly plan for same period: $79.92
Additional cost for annual plan: $20.07

One-week trial period: 2023-06-01 to 2023-06-08
Trial period cost: $9.99
```

Esta aplicação demonstra como nossa função `months_diff` pode ser usada em um cenário prático:

1.  Calculamos o custo total de uma assinatura com base no número de meses entre duas datas
2.  Comparamos esse custo com um plano anual para ajudar um usuário a decidir qual plano é mais econômico
3.  Calculamos o custo de um curto período de teste

Observe como mesmo o teste de 7 dias é cobrado como um mês inteiro em nosso modelo. Isso ocorre porque nossa função arredonda qualquer mês parcial para um mês inteiro, o que é comum na cobrança de assinaturas.

Este tipo de cálculo é frequentemente usado em:

- Serviços de assinatura (streaming, software, assinaturas)
- Cálculos de empréstimos e hipotecas
- Acordos de aluguel
- Faturamento de projetos
