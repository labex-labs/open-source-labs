# Compreendendo Objetos de Data em Python

Antes de calcular a diferença de meses entre datas, precisamos entender como trabalhar com objetos de data em Python. Nesta etapa, aprenderemos sobre o módulo `datetime` e criaremos alguns objetos de data.

Primeiro, vamos criar um novo arquivo Python no diretório do projeto. Abra a WebIDE e clique no ícone "New File" (Novo Arquivo) no painel do explorador no lado esquerdo. Nomeie o arquivo `month_difference.py` e salve-o no diretório `/home/labex/project`.

Agora, adicione o seguinte código para importar os módulos necessários:

```python
from datetime import date
from math import ceil

# Create example date objects
date1 = date(2023, 1, 15)  # January 15, 2023
date2 = date(2023, 3, 20)  # March 20, 2023

# Print the dates to see their format
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")

# Calculate the difference in days
day_difference = (date2 - date1).days
print(f"Difference in days: {day_difference}")
```

Salve o arquivo e execute-o usando o terminal:

```bash
python3 ~/project/month_difference.py
```

Você deve ver uma saída semelhante a esta:

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
```

A classe `date` do módulo `datetime` nos permite criar objetos de data especificando o ano, mês e dia. Quando subtraímos uma data de outra, o Python retorna um objeto `timedelta`. Podemos acessar o número de dias neste objeto usando o atributo `.days`.

Neste exemplo, há 64 dias entre 15 de janeiro de 2023 e 20 de março de 2023.
