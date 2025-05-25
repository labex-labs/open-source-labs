# Definir Funções Auxiliares

Definimos duas funções auxiliares. A primeira função, `to_ordinal`, converte um inteiro em uma string ordinal (por exemplo, 2 -> '2nd'). A segunda função, `format_score`, cria rótulos de pontuação para o eixo y direito como o nome do teste seguido pela unidade de medida (se houver), divididos em duas linhas.

```python
def to_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    return v + suffixes[v[-1]]

def format_score(score):
    return f'{score.value}\n{score.unit}' if score.unit else str(score.value)
```
