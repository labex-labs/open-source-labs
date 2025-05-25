# Exercício 1.7: Hipoteca do Dave (Dave's mortgage)

Dave decidiu contratar uma hipoteca de taxa fixa de 30 anos de \$500.000 com a Guido's Mortgage, Stock Investment, and Bitcoin trading corporation. A taxa de juros é de 5% e o pagamento mensal é de \$2684.11.

Aqui está um programa que calcula o valor total que Dave terá que pagar durante a vida da hipoteca:

```python
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)
```

Insira este programa e execute-o. Você deve obter a resposta `966279.5999999957`.
