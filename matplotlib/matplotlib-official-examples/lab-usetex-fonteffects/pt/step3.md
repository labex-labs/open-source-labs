# Definir a Função de Fonte

Nesta etapa, definiremos uma função que define a fonte. Esta função recebe o nome da fonte como argumento e retorna uma string que define a fonte para o nome especificado.

```python
def setfont(font):
    return rf'\font\a {font} at 14pt\a '
```
