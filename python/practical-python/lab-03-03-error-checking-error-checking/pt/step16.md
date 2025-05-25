# Exercício 3.10: Silenciando erros

Modifique a função `parse_csv()` para que as mensagens de erro de parsing possam ser silenciadas se explicitamente desejado pelo usuário. Por exemplo:

```python
>>> portfolio = parse_csv('missing.csv', types=[str,int,float], silence_errors=True)
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}]
>>>
```

O tratamento de erros é uma das coisas mais difíceis de acertar na maioria dos programas. Como regra geral, você não deve ignorar erros silenciosamente. Em vez disso, é melhor relatar problemas e dar ao usuário a opção de silenciar a mensagem de erro, caso ele escolha fazê-lo.
