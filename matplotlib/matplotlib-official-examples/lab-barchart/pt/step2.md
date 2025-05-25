# Preparar os Dados

Em seguida, prepararemos os dados para nosso gráfico. Temos três espécies de pinguins e três atributos, então criaremos um dicionário com as médias para cada atributo por espécie.

```python
species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
```
