# Preparar Dados

Precisamos definir as categorias e os resultados da pesquisa. Neste exemplo, temos uma pesquisa onde as pessoas avaliaram seu nível de concordância com perguntas em uma escala de cinco elementos. Definiremos as categorias como `category_names` e os resultados da pesquisa como `results`.

```python
category_names = ['Discordo totalmente', 'Discordo',
                  'Nem concordo nem discordo', 'Concordo', 'Concordo totalmente']
results = {
    'Question 1': [10, 15, 17, 32, 26],
    'Question 2': [26, 22, 29, 10, 13],
    'Question 3': [35, 37, 7, 2, 19],
    'Question 4': [32, 11, 9, 15, 33],
    'Question 5': [21, 29, 5, 5, 40],
    'Question 6': [8, 19, 5, 30, 38]
}
```
