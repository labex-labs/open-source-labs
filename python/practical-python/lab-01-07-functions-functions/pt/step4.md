# Capturando e Tratando Exceções

Exceções podem ser capturadas e tratadas.

Para capturar, use a instrução `try - except`.

```python
for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
    ...
```

O nome `ValueError` deve corresponder ao tipo de erro que você está tentando capturar.

É frequentemente difícil saber exatamente que tipos de erros podem ocorrer com antecedência, dependendo da operação que está sendo realizada. Para o bem ou para o mal, o tratamento de exceções geralmente é adicionado _depois_ que um programa travou inesperadamente (ou seja, "ah, esquecemos de capturar esse erro. Devemos tratá-lo!").
