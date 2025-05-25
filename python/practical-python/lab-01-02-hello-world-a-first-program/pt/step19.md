# Exercício 1.6: Depuração (Debugging)

O seguinte fragmento de código contém código do problema da Torre Sears. Ele também contém um erro.

```python
# sears.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

Copie e cole o código que aparece acima em um novo programa chamado `sears.py`. Quando você executar o código, receberá uma mensagem de erro que fará com que o programa trave, assim:

```code
Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
```

Ler mensagens de erro é uma parte importante do código Python. Se seu programa travar, a última linha da mensagem de traceback é a razão real pela qual o programa travou. Acima disso, você deve ver um fragmento do código-fonte e, em seguida, um nome de arquivo e número de linha identificadores.

- Qual linha contém o erro?
- Qual é o erro?
- Corrija o erro
- Execute o programa com sucesso
